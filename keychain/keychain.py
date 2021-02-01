import json
import uuid
import copy

from nodedata.node_data import PRIVATE_KEY

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature,
    decode_dss_signature
)
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

class Keychain:

    def __init__(self):
        self.address = str(uuid.uuid4())[0:8]
        
        self.private_key= serialization.load_pem_private_key(
            data=PRIVATE_KEY.encode('utf-8'),
            password=None,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        self.serialize_public_key()


    def serialize_public_key(self):

        self.public_key = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')[:-1]


    def serialize_private_key(self):

        self.private_key = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')


    def sign(self, data):

        return decode_dss_signature(self.private_key.sign(
            json.dumps(data).encode('utf-8'),
            ec.ECDSA(hashes.SHA256())))

    @staticmethod
    def check_signature(entry):

        public_key = entry.meta_data["public_key"]

        (r, s) = entry.meta_data["signature"]

        data = copy.deepcopy(entry.entry_data)
        data["entry_id"] = entry.entry_id

        deserialized_public_key = serialization.load_pem_public_key(
            public_key.encode('utf-8'),
            default_backend()
        )


        try:
            deserialized_public_key.verify(
                encode_dss_signature(r, s),
                json.dumps(data).encode('utf-8'),
                ec.ECDSA(hashes.SHA256())    
            )
            return True
        except InvalidSignature:
            return False


