from keychain.keychain import Keychain
import time
import copy


class Entry:

    def __init__(self):
        self.entry_id = None
        self.entry_data = None
        self.meta_data = None

    def __repr__(self):
        return (
            'Entry('
            f'entry_id: {self.entry_id}, '
            f'entry_data: {self.entry_data}, '
            f'meta_data: {self.meta_data} '
        )

    def gen_metadata(self, keychain, entry_data, entry_type):

        data = copy.deepcopy(entry_data)
        data["entry_id"] = self.entry_id
        signature =  keychain.sign(data)
        print("\nsigning Entry with local private Key ....")
        print("\npreparing meta data for entry ....")
        print("\nDONE")
        return {
            'timestamp': time.time_ns(),
            'public_key': keychain.public_key,
            'signature': signature,
            'entry_type' : entry_type
        }

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def to_json(self):
        return self.__dict__

    def check_entry(self, admin_keys, uni_keys_dict):

        if not Keychain.check_signature(self):
            raise Exception('Signatur ungültig')

        if self.requires_admin():
            if not self.from_admin_key(admin_keys):
                raise Exception(f'Nur Admin darf folgenden Eintrag machen: {self.entry_id}')

        if self.requires_uni():
            if self.entry_data["uni_id"] not in uni_keys_dict:
                raise Exception(f'Die Uni {self.entry_data["uni_id"]} ist nicht im System vorhanden')
            if not self.from_correct_uni_key(uni_keys_dict):
                raise Exception(f'Nur Uni {self.entry_data["uni_id"]} darf folgenden Eintrag machen: {self.entry_id}')


    def from_admin_key(self, admin_keys):
        if self.meta_data["public_key"] in admin_keys:
            return True
        return False

    def from_correct_uni_key(self, uni_keys_dict):
        if self.meta_data["public_key"] in uni_keys_dict[self.entry_data["uni_id"]]:
            return True
        return False


    def is_canceled(self, cancel_entries, entry_pool):
        for cancel_entry in cancel_entries:
            if self.entry_id == cancel_entry.entry_data["canceled_entry_id"]:

                if self.requires_admin():
                    entry_pool.delete_entry(cancel_entry)
                    raise Exception(f'Admineinträge kann man nicht annullieren')

                if self.entry_data["uni_id"] != cancel_entry.entry_data["uni_id"]:
                    entry_pool.delete_entry(cancel_entry)
                    raise Exception(f'Uni {cancel_entry.entry_data["uni_id"]} darf keine Einträge von Uni {self.entry_data["uni_id"]} löschen')

                if not cancel_entry.is_canceled(cancel_entries, entry_pool):
                    return True

        return False

    def requires_uni(self):
        if self.meta_data["entry_type"] == "matriculation" or self.meta_data["entry_type"] == "exmatriculation" or \
                self.meta_data["entry_type"] == "attempt" or self.meta_data["entry_type"] == "exam" or \
                self.meta_data["entry_type"] == "subject" or self.meta_data["entry_type"] == "cancel":
            return True
        return False

    def requires_admin(self):
        if self.meta_data["entry_type"] == "admin_key" or self.meta_data["entry_type"] == "uni_key" or \
                self.meta_data["entry_type"] == "student" or self.meta_data["entry_type"] == "uni" or \
                self.meta_data["entry_type"] == "revoke_key":
            return True
        return False

    def requires_student_id(self):
        if self.meta_data["entry_type"] == "matriculation" or \
                self.meta_data["entry_type"] == "student" or self.meta_data["entry_type"] == "exmatriculation":
            return True
        return False

