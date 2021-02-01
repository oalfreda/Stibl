import time
import uuid
from entry.entry import Entry

class Attempt_Entry(Entry):

    def __init__(
        self,
        keychain=None,
        entry_type=None,

        uni_id=None,
        m_number=None,
        exam_id=None,
        grade=None,

        entry_id=None,
        entry_data=None,
        meta_data=None
    ):
        if entry_id == None:
            self.entry_id = str(uuid.uuid4())[0:8]
        else:
            self.entry_id = entry_id

        if entry_data == None:
            self.entry_data = self.gen_entrydata(uni_id, m_number, exam_id, grade)
        else:
            self.entry_data = entry_data

        if meta_data == None:
            self.meta_data = self.gen_metadata(keychain, self.entry_data, entry_type)
        else:
            self.meta_data = meta_data

    def gen_entrydata(self, uni_id, m_number, exam_id, grade):

        return {
            'uni_id' : uni_id,
            'm_number': m_number,
            'exam_id' : exam_id,
            'grade': grade,
        }


