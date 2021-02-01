import threading
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from blockchain.blockchain import Blockchain
from blockchain.block import Block
from entry.entry import Entry
from utility.utility import json_to_entry

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-735dbff8-25d2-11eb-9c54-32dcb901e45f'
pnconfig.publish_key = 'pub-c-c8ff1447-7b70-4da0-bb77-2a5acdd7b1f0'

CHANNELS = [
    'ENTRY',
    'BLOCK',
    'CHAIN',
    'SYNC',
    'TEST'
]

class Listener(SubscribeCallback):
    def __init__(self, blockchain, keychain, entry_pool, chain_syncher, p2p):
        self.p2p = p2p

        self.blockchain = blockchain
        self.keychain = keychain
        self.entry_pool = entry_pool
        self.chain_syncher = chain_syncher

    def message(self, pubnub, message_object):

        if message_object.channel == 'BLOCK':
            sender_addr = message_object.message["sender_address"]
            if sender_addr != self.keychain.address:
                print(f'\nBlock empfangen von Node: {sender_addr} -> {Block.from_json(message_object.message["block"])}')
                block = Block.from_json(message_object.message["block"])
                new_chain = self.blockchain.chain[:]
                new_chain.append(block)
                try:
                    self.blockchain.replace_chain(Blockchain(new_chain), self.entry_pool)
                    self.entry_pool.filter(
                        self.blockchain
                    )
                    print('\nBlockchain ergänzt')
                except Exception as e:
                    print(f'\nFehler bei Ergänzung -> {e}')


        if message_object.channel == 'ENTRY':
            try:
                entry = json_to_entry(message_object.message)
                self.entry_pool.add_entry(entry)
                print(f'\nEintrag empfangen: {entry}')
            except Exception as e:
                print(f'\nFehler beim Empfangen eines Eintrags -> {e}')


        if message_object.channel == 'CHAIN':
            recipient_addr = message_object.message["recipient_address"]
            if recipient_addr == self.keychain.address:
                self.chain_syncher.add_chain(message_object.message["chain"])
                print('\nChain empfangen')


        if message_object.channel == 'SYNC':
            sender_addr = message_object.message["sender_address"]
            if self.keychain.address != sender_addr:
                self.p2p.send_chain(self.blockchain, sender_addr)
                print(f'\nChain gesendet an Node: {sender_addr}')

class P2P():

    def __init__(self, blockchain, keychain, entry_pool, chain_syncher):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS).execute()
        self.pubnub.add_listener(Listener(blockchain, keychain, entry_pool, chain_syncher, self))

        self.blockchain = blockchain
        self.keychain = keychain
        self.entry_pool = entry_pool
        self.chain_syncher = chain_syncher

    def publish(self, channel, message):
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_entry(self, entry):
        self.publish('ENTRY', entry.to_json())

    def broadcast_block(self, block):
        message = {"sender_address": self.keychain.address,
                   "block": block.to_json()}
        self.publish('BLOCK', message)

    def send_chain(self, chain, address):
        message= {"recipient_address": address,
                  "chain": chain.to_json()}
        self.publish('CHAIN', message)

    def sync_chain(self):
        message= {"sender_address": self.keychain.address}
        self.publish('SYNC', message)

        def wait_chains():
            try:
                new_chain_json = self.chain_syncher.get_chain()
                new_blockchain = Blockchain.from_json(new_chain_json)

                self.blockchain.replace_chain(new_blockchain, self.entry_pool)

                self.entry_pool.filter(self.blockchain)

                print('\nBlockchain synchronisiert')
            except Exception as e:
                print(f'\nBlockchain nicht synchronisiert -> {e}')

        threading.Timer(2.0, wait_chains).start()




