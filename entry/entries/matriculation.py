import time
import uuid
from keychain.keychain import Keychain
from entry.entry import Entry

class Matriculation_Entry(Entry):

    def __init__(
        self,
        keychain=None,
        entry_type=None,

        student_id=None,
        uni_id=None,
        m_number=None,

        entry_id=None,
        entry_data=None,
        meta_data=None
    ):
        if entry_id == None:
            self.entry_id = str(uuid.uuid4())[0:8]
        else:
            self.entry_id = entry_id

        if entry_data == None:
            self.entry_data = self.gen_entrydata(student_id, uni_id, m_number)
        else:
            self.entry_data = entry_data

        if meta_data == None:
            self.meta_data = self.gen_metadata(keychain, self.entry_data, entry_type)
        else:
            self.meta_data = meta_data

    def gen_entrydata(self, student_id, uni_id, m_number):

        return {
            'student_id': student_id,
            'uni_id': uni_id,
            'm_number' : m_number
        }





