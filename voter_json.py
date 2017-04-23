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

data = {
    'SH' : address1,
    'BJ' : address2,
    'NY' : address3
}

json_str = json.dumps(data)

with open('input.json', 'w') as f:
    json.dump(data, f)

pprint(data)

data1 = {
    'upper limit' : 4,
    'A' : outputs_address[0],
    'B' : outputs_address[1],
    'C' : outputs_address[2],
    'D' : outputs_address[3],
    'E' : outputs_address[4],
    'F' : outputs_address[5],
}

json_str = json.dumps(data1)

with open('output.json', 'w') as f:
    json.dump(data1, f)

pprint(data1)
