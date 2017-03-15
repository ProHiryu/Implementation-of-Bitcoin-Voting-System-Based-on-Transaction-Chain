from blockchain import blockexplorer
import time
import datetime
from blockchain import util

util.TIMEOUT = 5  # time out after 5 seconds

def set_time():

    # blocks = blockexplorer.get_blocks()
    #
    # for block in blocks:
    #     value = time.localtime(block.time)
    #     print (time.strftime("%Y-%m-%d %H:%M:%S", value))
    #     print (time.strftime("%a %b %d %H:%M:%S %Y", value))

    current_time = time.localtime(time.time())

    print ('Now is ' + time.strftime("%Y-%m-%d %H:%M:%S", current_time))

    # str_start_time = input('Please enter the start time')
    #
    # str_end_time = input('Please enter the end time')

    str_start_time_init = '2017-02-10 15:10:00'
    str_end_time_init = '2017-02-10 16:30:00'

    print('The time: ', str_start_time_init + ' - ', str_end_time_init)

    tuple_start_time_whole = time.strptime(
        str_start_time_init, '%Y-%m-%d %H:%M:%S')
    tuple_end_time_whole = time.strptime(str_end_time_init, '%Y-%m-%d %H:%M:%S')

    unix_start_time_whole = int(time.mktime(tuple_start_time_whole))
    unix_end_time_whole = int(time.mktime(tuple_end_time_whole))

    str_start_time = str_start_time_init[0:10] + ' 17:25:23'
    str_end_time = str_end_time_init[0:10] + ' 17:25:23'

    tuple_start_time = time.strptime(str_start_time, '%Y-%m-%d %H:%M:%S')
    tuple_end_time = time.strptime(str_end_time, '%Y-%m-%d %H:%M:%S')

    unix_start_time = int(time.mktime(tuple_start_time))
    unix_end_time = int(time.mktime(tuple_end_time))

    print(unix_end_time, unix_start_time)


    blocks = blockexplorer.get_blocks(time=(unix_start_time * 1000 + 455))

    # for block in blocks:
    #     value = time.localtime(block.time)
    #     print(block.time)
    #     print (time.strftime("%Y-%m-%d %H:%M:%S", value))
    #     print (time.strftime("%a %b %d %H:%M:%S %Y", value))
    #
    # # blocks = blockexplorer.get_blocks()
    # #
    # # for block in blocks:
    # #     print (block.time)
    #
    #
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1487841923)))

    start_height = blocks[0].height
    block = blocks[0]

    if block.time < unix_start_time_whole:
        while(block.time < unix_start_time_whole):
            start_height += 3
            blockss = blockexplorer.get_block_height(start_height)
            block = blockss[0]
            print(block.time, unix_start_time_whole)
    else:
        while(block.time > unix_start_time_whole):
            start_height += 3
            blockss = blockexplorer.get_block_height(start_height)
            block = blockss[0]
            print(block.time, unix_start_time_whole)

    print(start_height)

    blocks = blockexplorer.get_blocks(time=(unix_end_time * 1000 + 455))

    end_height = blocks[0].height
    block = blocks[0]


    if block.time < unix_end_time_whole:
        while(block.time < unix_end_time_whole):
            end_height += 3
            blockss = blockexplorer.get_block_height(end_height)
            block = blockss[0]
            print(block.time, unix_end_time_whole)
    else:
        while(block.time > unix_end_time_whole):
            end_height += 3
            blockss = blockexplorer.get_block_height(end_height)
            block = blockss[0]
            print(block.time, unix_end_time_whole)

    print(end_height)

    return start_height,end_height
