import json
import uuid

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

def serialize_public_key(pub_key):

    public_key = pub_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
    return public_key
        
def serialize_private_key(pri_key):
    private_key = pri_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()).decode('utf-8')
    return private_key

private_key = ec.generate_private_key(
            ec.SECP256K1(),
            default_backend()
        )
public_key = private_key.public_key()

public_key = serialize_public_key(public_key)
private_key = serialize_private_key(private_key)
print(public_key)
print(private_key)





