from utility.utility import sha256_hash

ADMIN_KEYS = [
"""-----BEGIN PUBLIC KEY-----
MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEniJVwRr3qoIyP177stzchl79eWqh5xog
3iU7QA5RUJwy/FqDRlcxVLlm82XrByqybKu687/3Dm65LWldQA0lXQ==
-----END PUBLIC KEY-----"""
]

UNIS = [
    {"id": "JGU", "name": "Johannes Gutenberg Universität","keys":[
"""-----BEGIN PUBLIC KEY-----
MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEBwZTOQzNNdA9c3zBtg3jzVQh1IqCwORE
LwkFVqVR39ra9H3s3aan1yYw5D30LcIJEBPZxQD56e5hz5mqqgrifg==
-----END PUBLIC KEY-----"""]},

    {"id": "TUD", "name": "Technische Universität Darmstadt", "keys": [
"""-----BEGIN PUBLIC KEY-----
MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAErujwKNjTdvZhljNDMleU4NO/9ZpCtek1
XNqU4ipBbbmbrpQ0h/1Q4iTlyRrEEneK1wRTDxKvrbIkSXmHhDvovQ==
-----END PUBLIC KEY-----"""]},

    {"id": "HRM", "name": "Hochschule RheinMain", "keys":[
"""-----BEGIN PUBLIC KEY-----
MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEV4Y9rpXQr3AqmHxmR2XPiZpKtPsmkuJA
Ix4MsnvNAb/iFW9iwK2VojhCfczzge4qzUGLofOwMpmDR2XZhBeojg==
-----END PUBLIC KEY-----"""]},

    {"id": "JWGU", "name": "Johann Wolfgang Goethe-Universität", "keys":[
"""-----BEGIN PUBLIC KEY-----
MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE+jTmwFb64nBT/+wGHF7Sqk4Bbk0dqa6v
MD7Nc3Y5vwLqM7ofc92Ma+52zM6xsV0QtkcVPCoeJbwVGxq3+pLCbg==
-----END PUBLIC KEY-----"""]}]

GENESIS_TIMESTAMP = 1

GENESIS_LAST_HASH = 'genesis_last_hash'

GENESIS_DATA = [{"admin_keys" : ADMIN_KEYS, "unis" : UNIS, "meta_data":{"entry_type" : "genesis"}}]

GENESIS_DIFFICULTY = 16

GENESIS_NONCE = 'genesis_nonce'

GENESIS_HASH = sha256_hash(GENESIS_TIMESTAMP, GENESIS_LAST_HASH, GENESIS_DATA, GENESIS_DIFFICULTY, GENESIS_NONCE)


GENESIS_BLOCK_DATA = {
    'timestamp': GENESIS_TIMESTAMP,
    'last_hash': GENESIS_LAST_HASH,
    'hash': GENESIS_HASH,
    'data': GENESIS_DATA,
    'difficulty': GENESIS_DIFFICULTY,
    'nonce': GENESIS_NONCE
}