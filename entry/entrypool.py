class Entry_Pool:
    def __init__(self):
        self.pool = {}

    def add_entry(self, entry):
        self.pool[entry.entry_id] = entry


    def get_entries_json(self):
        return list(map(lambda entry: entry.to_json(), self.pool.values()))

    def delete_entry(self, entry):
        try:
            del self.pool[entry.entry_id]
            print(f"\nEintrag {entry.entry_id} vom lokalen Pool gelöscht")
        except KeyError:
            pass

    def filter(self, blockchain):
        for block in blockchain.chain[1:]:
            for entry in block.data:
                try:
                    del self.pool[entry.entry_id]
                except KeyError:
                    pass