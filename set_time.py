from blockchain import blockexplorer
import time
import datetime

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

str_start_time = '2017-02-10 15:10:00'
str_end_time = '2017-02-10 16:30:00'

tuple_start_time = time.strptime(str_start_time, '%Y-%m-%d %H:%M:%S')
tuple_end_time = time.strptime(str_end_time, '%Y-%m-%d %H:%M:%S')

unix_start_time = int(time.mktime(tuple_start_time))
unix_end_time = int(time.mktime(tuple_end_time))

print(unix_end_time, unix_start_time)

blocks = blockexplorer.get_blocks(time=1489107043)

for block in blocks:
    value = time.localtime(block.time)
    print(block.time)
    print (time.strftime("%Y-%m-%d %H:%M:%S", value))
    print (time.strftime("%a %b %d %H:%M:%S %Y", value))
