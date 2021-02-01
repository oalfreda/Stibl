from utility.utility import sha256_hash
class Chain_Syncher:

    def __init__(self):
        self.inventory = {}
        self.counter = {}

    def add_chain(self, chain):
        hashed_chain = sha256_hash(chain)
        self.inventory[hashed_chain] = chain
        if hashed_chain not in self.counter.keys():
            self.counter[hashed_chain] = 1
        else:
            self.counter[hashed_chain] += 1

    def clear(self):
        self.inventory = {}
        self.counter = {}

    def get_chain(self):
        if self.inventory == {} or self.counter == {}:
            raise Exception("ChainSyncher ist leer")
        max = 0
        winner_hash = None
        for hash in self.counter:
            if self.counter[hash] > max:
                max = self.counter[hash]
                winner_hash = hash
        result = self.inventory[winner_hash]
        self.clear()
        return result




