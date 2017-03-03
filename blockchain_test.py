from blockchain import blockexplorer

# block = blockexplorer.get_block(
#     '000000000000000016f9a2c3e0f4c1245ff24856a79c34806969f5084f410680')
#
# tx = blockexplorer.get_tx(
#     'd4af240386cdacab4ca666d178afc88280b620ae308ae8d2585e9ab8fc664a94')
#
# blocks = blockexplorer.get_block_height(2570)
#
# address = blockexplorer.get_address('1HS9RLmKvJ7D1ZYgfPExJZQZA1DMU3DEVd')
#
# outs = blockexplorer.get_unspent_outputs('1HS9RLmKvJ7D1ZYgfPExJZQZA1DMU3DEVd')
#
# latest_block = blockexplorer.get_latest_block()
#
# txs = blockexplorer.get_unconfirmed_tx()

latest_block = blockexplorer.get_latest_block()

block = blockexplorer.get_block(latest_block.hash)
transactions = []

transactions = block.transactions

for transaction in transactions:
    inputs = transaction.inputs
    outputs = transaction.outputs
    for ip in inputs:
        try:
            print('- - - - -' + ip.address)
        except AttributeError:
            print ('')
    for op in outputs:
        print (op.address)

# print (latest_block.hash,latest_block.time,latest_block.height,latest_block.block_index)
