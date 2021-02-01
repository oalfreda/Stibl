from flask import Flask, Response, render_template
import sys
import time
import json

from blockchain.blockchain import Blockchain
from keychain.keychain import Keychain
from entry.entrypool import Entry_Pool
from chainsyncher.chainsyncher import Chain_Syncher
from p2p.p2p import P2P


from api_routes import *

#Initialisiere die Blockchain, die Eintragslliste, den Schlüsselbund, den Chainholder, und das simulierte P2P Netzwerk(PubNub)
blockchain = Blockchain()
keychain = Keychain()
entry_pool = Entry_Pool()
chain_syncher = Chain_Syncher()
p2p = P2P(blockchain, keychain, entry_pool, chain_syncher)

#Initialisiere das Python-Backend und die zugehörigen Schnittstellen
node = Flask(__name__)
node.config['JSON_SORT_KEYS'] = False
node.register_blueprint(construct_post_blueprint(keychain, p2p))
node.register_blueprint(construct_data_blueprint(blockchain, keychain, entry_pool))
node.register_blueprint(construct_util_blueprint(blockchain, entry_pool, p2p))

#Synchronisiere die Node
p2p.sync_chain()


@node.route('/')
def index():
    return render_template('index.html', p=str(sys.argv[1]))


@node.route('/home')
def index2():
    return render_template('index.html', p=str(sys.argv[1]))


#Starte den Server
node.run(threaded=True, debug=False, host='0.0.0.0', port=sys.argv[1])













