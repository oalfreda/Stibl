from flask import Blueprint, render_template
from blockchain.block import Block



def construct_util_blueprint(blockchain, entry_pool, p2p):
    util_methods = Blueprint('util_methods', __name__)

    @util_methods.route('/mine')
    def util_mine():
        entry_json_list = entry_pool.get_entries_json()
        new_block = Block.mine_block(blockchain.chain[-1], entry_json_list)
        print(f"\nneuer Block: {new_block}")
        blockchain.chain.append(new_block)

        p2p.broadcast_block(new_block)
        entry_pool.filter(blockchain)

        return render_template("pool_site.html")


    return util_methods
