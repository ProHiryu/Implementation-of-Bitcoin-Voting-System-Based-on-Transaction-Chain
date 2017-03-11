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

str_start_time_init = '2017-02-10 15:10:00'
str_end_time_init = '2017-02-10 16:30:00'

str_start_time = str_start_time_init[0:10] + ' 17:25:23'
str_end_time = str_end_time_init[0:10] + ' 17:25:23'


print('The time: ',str_start_time+ ' - ',str_end_time)

tuple_start_time = time.strptime(str_start_time, '%Y-%m-%d %H:%M:%S')
tuple_end_time = time.strptime(str_end_time, '%Y-%m-%d %H:%M:%S')

unix_start_time = int(time.mktime(tuple_start_time))
unix_end_time = int(time.mktime(tuple_end_time))

print(unix_end_time, unix_start_time)


blocks = blockexplorer.get_blocks(time=(unix_start_time * 1000 + 455))

for block in blocks:
    value = time.localtime(block.time)
    print(block.time)
    print (time.strftime("%Y-%m-%d %H:%M:%S", value))
    print (time.strftime("%a %b %d %H:%M:%S %Y", value))

# blocks = blockexplorer.get_blocks()
#
# for block in blocks:
#     print (block.time)


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1487841923)))
