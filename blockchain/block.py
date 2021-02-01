import time
from utility.utility import sha256_hash, json_to_entry
from utility.utility import hexa_to_binary
from nodedata.node_data import MINE_RATE
from nodedata.genesis_data import GENESIS_BLOCK_DATA


class Block:

    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})'
        )

    @staticmethod
    def mine_block(last_block, entry_json_list):

        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = last_block.gen_difficulty(timestamp)
        nonce = 0
        hash = sha256_hash(timestamp, last_hash, entry_json_list, difficulty, nonce)

        while hexa_to_binary(hash)[0:difficulty] != '0' * difficulty:
            print(f"\n{hash} -> Proof of Work nicht erfüllt, setzte nonce auf {nonce +1}")
            nonce += 1
            timestamp = time.time_ns()
            difficulty = last_block.gen_difficulty(timestamp)
            hash = sha256_hash(timestamp, last_hash, entry_json_list, difficulty, nonce)
            #print(hexa_to_binary(hash)[0:difficulty])
        print(f"\n{hash} -> GÜLTIGER HASH GEFUNDEN")
        data = list(map(lambda entry_json: json_to_entry(entry_json), entry_json_list))
        return Block(timestamp, last_hash, hash, data, difficulty, nonce)



    @staticmethod
    def genesis():
        return Block(**GENESIS_BLOCK_DATA)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def to_json(self):
        if self.timestamp == 1:
            data = self.data
        else:
            data = list(map(lambda entry: entry.to_json(), self.data))
        return {
            "timestamp" : self.timestamp ,
            "last_hash" : self.last_hash,
            "hash" : self.hash,
            "data" : data,
            "difficulty" : self.difficulty,
            "nonce" : self.nonce
        }

    @staticmethod
    def from_json(block_json):
        if block_json["last_hash"] == 'genesis_last_hash':
            data = block_json["data"]
        else:
            data = list(
                map(lambda entry_json: json_to_entry(entry_json), block_json["data"])
            )

        block = Block(block_json["timestamp"], block_json["last_hash"], block_json["hash"], data,
                      block_json["difficulty"], block_json["nonce"])

        return block

    def check_block(self, last_block):
        if self.last_hash == 'genesis_last_hash':
            data = self.data
        else:
            data = list(map(lambda entry: entry.to_json(), self.data))

        if self.last_hash != last_block.hash:
            raise Exception('Last_hash stimmmt nicht überein')

        if hexa_to_binary(self.hash)[0:self.difficulty] != '0' * self.difficulty:
            raise Exception('Anzahl Nullen stimmt nicht überein')

        if abs(last_block.difficulty - self.difficulty) > 1:
            raise Exception('Difficulty wurde um mehr als eins verändert')

        hash_reconstructed = sha256_hash(
            self.timestamp,
            self.last_hash,
            data,
            self.nonce,
            self.difficulty
        )

        if self.hash != hash_reconstructed:
            raise Exception('Hash stimmt nicht überein')


    def gen_difficulty(self, timestamp):

        if (timestamp - self.timestamp) < MINE_RATE:
            return self.difficulty + 1

        if (self.difficulty - 1) > 0:
            return self.difficulty - 1

        return 1
