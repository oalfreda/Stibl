import hashlib
import json

from entry import Attempt_Entry, Cancel_Entry, Exam_Entry, Exmatriculation_Entry, Matriculation_Entry, Student_Entry, \
    Subject_Entry, University_Entry, Admin_Key_Entry, Uni_Key_Entry, Revoke_Key_Entry


def hexa_to_binary(hexa_string):

    end_length = len(hexa_string) * 4

    hex_as_int = int(hexa_string, 16)

    hex_as_binary = bin(hex_as_int)

    padded_binary = hex_as_binary[2:].zfill(end_length)

    return padded_binary


def sha256_hash(*data_args):

    data_args_sorted = sorted(map(lambda data: json.dumps(data), data_args))
    data_joined = ''.join(data_args_sorted)
    return hashlib.sha256(data_joined.encode('utf-8')).hexdigest()


def json_to_entry(entry_json):
    if entry_json["meta_data"]["entry_type"] == "attempt":
        return Attempt_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    elif entry_json["meta_data"]["entry_type"] == "cancel":
        return Cancel_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    elif entry_json["meta_data"]["entry_type"] == "exam":
        return Exam_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    elif entry_json["meta_data"]["entry_type"] == "exmatriculation":
        return Exmatriculation_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    elif entry_json["meta_data"]["entry_type"] == "matriculation":
        return Matriculation_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    elif entry_json["meta_data"]["entry_type"] == "student":
        return Student_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    elif entry_json["meta_data"]["entry_type"] == "subject":
        return Subject_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    elif entry_json["meta_data"]["entry_type"] == "uni":
        return University_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    elif entry_json["meta_data"]["entry_type"] == "admin_key":
        return Admin_Key_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    elif entry_json["meta_data"]["entry_type"] == "uni_key":
        return Uni_Key_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    elif entry_json["meta_data"]["entry_type"] == "revoke_key":
        return Revoke_Key_Entry(entry_id=entry_json["entry_id"], entry_data=entry_json["entry_data"], meta_data=entry_json["meta_data"])
    else:
        raise Exception("Unbekannter Eintragstyp, Eintrag wurde verworfen")