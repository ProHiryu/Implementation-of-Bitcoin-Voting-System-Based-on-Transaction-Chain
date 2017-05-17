import json
from pprint import pprint

inputs_address = []
outputs_address = []

input_file = open('voters.txt', 'r')
output_file = open('candidates.txt', 'r')

for line in input_file.readlines():
    line = line.strip()
    inputs_address.append(line)

for line in output_file.readlines():
    line = line.strip()
    outputs_address.append(line.split(' : ')[0])

address1 = inputs_address[:17]
address2 = inputs_address[18:37]
address3 = inputs_address[23:35]

data1 = {
    'Location': 'SH',
    'Addresses': address1
}

data2 = {
    'Location': 'BJ',
    'Addresses': address2
}

data3 = {
    'Location': 'NY',
    'Addresses': address3
}

data = {
    'Name': 'Voting',
    'Time': '2017-05-12',
    'Contractor': 'SJTU',
    'Data': [data1, data2, data3]
}

json_str = json.dumps(data)

with open('input.json', 'w') as f:
    json.dump(data, f)

pprint(data)

data2 = {
    'Name': 'A',
    'Address': outputs_address[0]
}
data3 = {
    'Name': 'B',
    'Address': outputs_address[1]
}
data4 = {
    'Name': 'C',
    'Address': outputs_address[2]
}
data5 = {
    'Name': 'D',
    'Address': outputs_address[3]
}
data6 = {
    'Name': 'E',
    'Address': outputs_address[4]
}
data7 = {
    'Name': 'F',
    'Address': outputs_address[5]
}

data1 = {
    'Upper limit': 4,
    'Type': 1,
    'Numbers': 6,
    'Data': [data2, data3, data4, data5, data6, data7]
}

json_str = json.dumps(data1)

with open('output.json', 'w') as f:
    json.dump(data1, f)

pprint(data1)
