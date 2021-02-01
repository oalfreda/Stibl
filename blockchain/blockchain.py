from blockchain.block import Block
from collections import namedtuple
import copy

class Blockchain:

    def __init__(self,chain=[Block.genesis()]):
        self.chain = chain


    def to_json(self):
        return  list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def from_json(chain_json):
        blockchain = Blockchain()
        blockchain.chain =list(
            map(lambda block_json: Block.from_json(block_json), chain_json)
        )
        return blockchain

    def replace_chain(self, blockchain, entry_pool):
        try:
            if len(blockchain.chain) <= len(self.chain):
                raise Exception("neue Blockchain hat die selbe oder kleinere Länge")
            blockchain.check_chain(entry_pool)
        except Exception as e:
            raise Exception(f"Ungültige Blockchain -> {e}")
        self.chain = blockchain.chain


    def check_chain(self, entry_pool):
        if self.chain[0] != Block.genesis():
            raise Exception("Kein gültiger Genesis-Block")
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            last_block = self.chain[i-1]
            block.check_block(last_block)
        self.check_entries(entry_pool)


    def check_entries(self, entry_pool):
        entry_ids = set()

        admin_keys = copy.deepcopy(self.chain[0].data[0]["admin_keys"])

        uni_keys_dict = {}
        for genesis_uni in self.chain[0].data[0]["unis"]:
            uni_keys_dict[genesis_uni["id"]] = copy.deepcopy(genesis_uni["keys"])

        cancel_entries = self.get_cancels()
        matric_entries, exmatric_entries, attempt_entries, subject_entries, exam_entries = self.get_relevant_entries(cancel_entries, entry_pool)
        self.check_attempts(entry_pool,attempt_entries)

        for i in range(1, len(self.chain)):
            block = self.chain[i]
            for entry in block.data:
                try:
                    #Prüfe den Eintrag auf Validität
                    entry.check_entry(admin_keys, uni_keys_dict)

                    #Prüfe den Key auf Einzigartigkeit
                    if entry.entry_id in entry_ids:
                        raise Exception(f"Eintrag {entry.entry_id} nicht einzigartig")
                    entry_ids.add(entry.entry_id)

                    #Füge den Key den aktuellen Admin-Keys hinzu
                    if entry.meta_data["entry_type"] == "admin_key":
                        admin_keys.append(entry.entry_data["key"])

                    #Registriert eine Uni im System
                    if entry.meta_data["entry_type"] == "uni":
                        if entry.entry_data["uni_id"] not in uni_keys_dict.keys():
                            uni_keys_dict[entry.entry_data["uni_id"]] = []
                        else:
                            raise Exception(f"Eine Uni mit Id: {entry.entry_data['uni_id']} gibt es bereits")

                    #Füge den Key den aktuellen Uni-Keys hinzu
                    if entry.meta_data["entry_type"] == "uni_key":

                        if entry.entry_data["uni_id"] not in uni_keys_dict.keys():
                            raise Exception(f"Keine Uni mit Id: {entry.entry_data['uni_id']} im System registriert")
                        else:
                            uni_keys_dict[entry.entry_data["uni_id"]].append(entry.entry_data["key"])

                    #Entferne Key-Berechtigungen, ab diesem Moment in der Chain
                    if entry.meta_data["entry_type"] == "revoke_key":

                        if entry.entry_data["key"] in admin_keys:
                            admin_keys.remove(entry.entry_data["key"])
                        for uni in uni_keys_dict:
                            if entry.entry_data["key"] in uni_keys_dict[uni]:
                                uni_keys_dict[uni].remove(entry.entry_data["key"])


                except Exception as e:

                    #Im Falle, dass der Eintrag zu Fehlern geführt hat, wird dieser vom lokalen Pool entfernt
                    entry_pool.delete_entry(entry)
                    raise Exception(f" Fehlerhafter Eintrag -> {e}")




    def get_cancels(self):
        cancel_entries = []
        for i in range(1, len(self.chain)):

            block = self.chain[i]
            for entry in block.data:

                if entry.meta_data["entry_type"] == "cancel":
                    cancel_entries.append(entry)
        return cancel_entries


    def get_relevant_entries(self, cancel_entries, entry_pool):
        matric = []
        exmatric = []
        attempt = []
        subject = []
        exam = []
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            for entry in block.data:
                if entry.is_canceled(cancel_entries, entry_pool):
                    continue
                if entry.meta_data["entry_type"] == "matriculation":
                        matric.append(entry)
                if entry.meta_data["entry_type"] == "exmatriculation":
                        exmatric.append(entry)
                if entry.meta_data["entry_type"] == "attempt":
                        attempt.append(entry)
                if entry.meta_data["entry_type"] == "subject":
                        subject.append(entry)
                if entry.meta_data["entry_type"] == "exam":
                        exam.append(entry)

        return matric, exmatric, attempt, subject, exam



#schaut ob ein Student in der Blockchain eine Klausur bereits mehr als 3 mal nicht bestanden hat

    def check_attempts(self,entry_pool, attempt_entries):
        Attempt = namedtuple("Attempt", ["student", "exam"])
        Attempt_dict = {}

        for attempt_entry in attempt_entries:
            try:
                st = attempt_entry.entry_data["m_number"]
                ex = attempt_entry.entry_data["exam_id"]
                grade = attempt_entry.entry_data["grade"]

                if Attempt(st, ex) not in Attempt_dict.keys():
                    Attempt_dict[Attempt(st, ex)] = [grade]
                elif len(Attempt_dict[Attempt(st, ex)]) >= 3 :
                    raise Exception(f"Student {st} hat die Klausur {ex} schon dreimal geschrieben")
                elif Attempt_dict[Attempt(st, ex)][-1] != "5.0" :
                    raise Exception(f"Student {st} hat die Klausur {ex} schon einmal bestanden")
                else:
                    Attempt_dict[Attempt(st, ex)].append(grade)
            except Exception as e:

                # Im Falle, dass der Eintrag zu Fehlern geführt hat, wird dieser vom lokalen Pool entfernt
                entry_pool.delete_entry(attempt_entry)
                raise Exception(f" Fehlerhafter Versuch -> {e}")



    def get_student_history(self, student_id):
        mat = []
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            for entry in block.data:
                if entry.meta_data["entry_type"] == "matriculation" or entry.meta_data["entry_type"] == "exmatriculation":
                    if entry.entry_data["student_id"] == student_id:
                        mat.append(entry.entry_data["m_number"])


        history = []
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            for entry in block.data:
                if entry.requires_student_id():
                    if entry.entry_data["student_id"] == student_id:
                        history.append(entry.to_json())
                if entry.meta_data["entry_type"] == "attempt":
                    if entry.entry_data["m_number"] in mat:
                        history.append(entry.to_json())
        return history









