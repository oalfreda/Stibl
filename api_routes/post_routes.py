from flask import Blueprint, request, jsonify, render_template
from entry import *
import codecs


def construct_post_blueprint(keychain,p2p):

    post_methods = Blueprint('post_methods', __name__)

    @post_methods.route('/transact_entry', methods=['POST'])
    def post_entry():

        post_data = request.form
        print("received Entry Data -> preparing Entry ...")
        if post_data.get("entry_type") == "attempt":
            entry = Attempt_Entry(
                keychain,
                post_data.get("entry_type"),
                post_data.get("uni_id"),
                post_data.get("m_number"),
                post_data.get("exam_id"),
                post_data.get("grade")
            )
        elif post_data.get("entry_type") == "cancel":
            entry = Cancel_Entry(
                keychain,
                post_data.get("entry_type"),
                post_data.get("canceled_entry_id"),
                post_data.get("uni_id")
            )
        elif post_data.get("entry_type") == "exam":
            entry = Exam_Entry(
                keychain,
                post_data.get("entry_type"),
                post_data.get("exam_id"),
                post_data.get("uni_id"),
                post_data.get("name"),
                post_data.get("subject_id")
            )
        elif post_data.get("entry_type") == "exmatriculation":
            entry = Exmatriculation_Entry(
                keychain,
                post_data.get("entry_type"),
                post_data.get("student_id"),
                post_data.get("uni_id"),
                post_data.get("m_number")
            )
        elif post_data.get("entry_type") == "matriculation":
            entry = Matriculation_Entry(
                keychain,
                post_data.get("entry_type"),
                post_data.get("student_id"),
                post_data.get("uni_id"),
                post_data.get("m_number")
            )
        elif post_data.get("entry_type") == "student":
            entry = Student_Entry(
                keychain,
                post_data.get("entry_type"),
                post_data.get("student_id"),
                post_data.get("name"),
            )
        elif post_data.get("entry_type") == "subject":
            entry = Subject_Entry(
                keychain,
                post_data.get("entry_type"),
                post_data.get("subject_id"),
                post_data.get("uni_id"),
                post_data.get("name")
            )
        elif post_data.get("entry_type") == "uni":
            entry = University_Entry(
                keychain,
                post_data.get("entry_type"),
                post_data.get("uni_id"),
                post_data.get("name")
            )
        elif post_data.get("entry_type") == "admin_key":
            entry = Admin_Key_Entry(
                keychain,
                post_data.get("entry_type"),
                codecs.decode(post_data.get("key"), 'unicode_escape')
            )
            print(post_data.get("key"))
        elif post_data.get("entry_type") == "uni_key":
            entry = Uni_Key_Entry(
                keychain,
                post_data.get("entry_type"),
                post_data.get("uni_id"),
                codecs.decode(post_data.get("key"), 'unicode_escape')
            )
            print(post_data.get("key"))
        elif post_data.get("entry_type") == "revoke_key":
            entry = Revoke_Key_Entry(
                keychain,
                post_data.get("entry_type"),
                codecs.decode(post_data.get("key"), 'unicode_escape')
            )

        else:
            raise Exception("Unbekannter Eintragstyp")
        p2p.broadcast_entry(entry)
        print(f"\nEntry prepared: {entry}")

        return render_template(f'/entries/{post_data.get("entry_type")}_entry.html', success = "true")

        #return jsonify(entry.to_json())

    return post_methods