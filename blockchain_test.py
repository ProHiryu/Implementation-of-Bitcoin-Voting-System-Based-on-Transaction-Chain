from blockchain import blockexplorer
from set_time import set_time
from set_candidates import set_candidates
from blockchain import util

util.TIMEOUT = 5  # time out after 5 seconds

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

start_height, end_height = set_time()

# latest_block = blockexplorer.get_latest_block()
#
# latest_height = latest_block.height

print(start_height,end_height)

blocks = []

for height in range(start_height, end_height):
    blockss = blockexplorer.get_block_height(height)
    block = blockss[0]
    blocks.append(block)

inputs_address = []
outputs_address = []

for block in blocks:
    transactions = []
    transactions = block.transactions

    for transaction in transactions:
        inputs = transaction.inputs
        outputs = transaction.outputs
        inputs_temp = []
        for ip in inputs:
            try:
                inputs_temp.append(ip.address)
            except AttributeError:
                print ('woops')

        inputs_address.append(inputs_temp)

        # try:
        #     print('- - - - - input address : ' + ip.address)
        #     print('- - - - - input value : ' + str(ip.value))
        #     print('- - - - - input tx_index : ' + str(ip.tx_index))
        #     print('- - - - - input n : ' + str(ip.n))
        #     print('- - - - - input type :' + str(ip.type))
        # except AttributeError:
        #     print ('')

        outputs_temp = []
        for op in outputs:
            outputs_temp.append(op.address)

        outputs_address.append(outputs_temp)

        # print('output address : ' + str(op.address))
        # print('output value : ' + str(op.value))
        # print('output n : ' + str(op.n))
        # print('ouput tx_index : ' + str(op.tx_index))
        # print(op.spent)

# # show all the data
#
# for i in range(len(inputs_address)):
#     if len(outputs_address[i]) > 1:
#         continue
#     else:
#         print('The No.' + str(i + 1) + 'transaction')
#         for address in inputs_address[i]:
#             print('The input address: ' + str(address))
#         for address in outputs_address[i]:
#             print('The output address: ' + str(address))
#         print('')


voters = []
candidates = []

for i in range(len(outputs_address)):
    for address in outputs_address[i]:
        if address not in candidates:
            candidates.append(address)

for i in range(len(inputs_address)):
    if len(outputs_address[i]) > 1:
        continue
    else:
        for address in inputs_address[i]:
            if address not in voters:
                voters.append(address)
                candidates.append(outputs_address[i][0])


# print candidates

# for candidate in candidates:
#     print (candidate)

results = dict()

for candidate in set(candidates):
    results[candidate] = candidates.count(candidate)

last = sorted(results.items(), key=lambda t: t[1], reverse=True)

for (x, y) in last:
    if y > 10:
        print(x, ' : ', y)


# print (latest_block.hash,latest_block.time,latest_block.height,latest_block.block_index)
