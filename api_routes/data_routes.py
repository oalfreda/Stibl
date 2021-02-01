from flask import Blueprint, jsonify, render_template, request, Response
import json
import time



def construct_data_blueprint(blockchain, keychain, entrylist):
    data_methods = Blueprint('data_methods', __name__)

    @data_methods.route('/chain')
    def data_blockchain():
        return jsonify(blockchain.to_json())

    @data_methods.route('/address')
    def data_address():
        return jsonify({'address': keychain.address})

    @data_methods.route('/entries')
    def data_entries():
        return jsonify(entrylist.get_entries_json())

    @data_methods.route('/transact_query/student_history')
    def data_history():
        student_id = request.args.get('student_id')
        result = blockchain.get_student_history(student_id)
        print(result)
        return render_template('/entries_query.html', jsonfile = json.dumps(result))

    @data_methods.route('/blockchain')
    def get_blockchain_site():
        return render_template('blockchain_site.html')

    @data_methods.route('/entry/uni')
    def get_uni_entry_site():
        return render_template('/entries/uni_entry.html')

    @data_methods.route('/entry/admin_key')
    def get_admin_key_entry_site():
        return render_template('/entries/admin_key_entry.html')

    @data_methods.route('/entry/uni_key')
    def get_uni_key_entry_site():
        return render_template('/entries/uni_key_entry.html')

    @data_methods.route('/entry/revoke_key')
    def get_revoke_key_entry_site():
        return render_template('/entries/revoke_key_entry.html')

    @data_methods.route('/entry/attempt')
    def get_attempt_entry_site():
        return render_template('/entries/attempt_entry.html')

    @data_methods.route('/entry/cancel')
    def get_cancel_entry_site():
        return render_template('/entries/cancel_entry.html')

    @data_methods.route('/entry/exam')
    def get_exam_entry_site():
        return render_template('/entries/exam_entry.html')

    @data_methods.route('/entry/exmatriculation')
    def get_exmatriculation_entry_site():
        return render_template('/entries/exmatriculation_entry.html')

    @data_methods.route('/entry/matriculation')
    def get_matriculation_entry_site():
        return render_template('/entries/matriculation_entry.html')

    @data_methods.route('/entry/student')
    def get_student_entry_site():
        return render_template('/entries/student_entry.html')

    @data_methods.route('/entry/subject')
    def get_subject_entry_site():
        return render_template('/entries/subject_entry.html')

    @data_methods.route('/pool')
    def get_mine_site():
        return render_template('pool_site.html', jsonfile=json.dumps(entrylist.get_entries_json()))

    @data_methods.route('/query/student_history')
    def ok():
        return render_template('queries/student_history.html')

    @data_methods.route('/stream/blockchain')
    def chain_stream():
        def stream_chain():
            while True:
                time.sleep(1)
                yield f'data: {blockchain.to_json()}\n\n'

        return Response(stream_chain(), mimetype="text/event-stream")

    @data_methods.route('/stream/entrypool')
    def pool_stream():
        def stream_pool():
            while True:
                time.sleep(1)
                yield f'data: {entrylist.get_entries_json()}\n\n'

        return Response(stream_pool(), mimetype="text/event-stream")

    return data_methods



