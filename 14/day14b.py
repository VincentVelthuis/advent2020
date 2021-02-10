import sys, fileinput
lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]

mask = ''
memory = {}

def split_address(num):
    value = '{:0{}b}'.format(num,len(mask))
    result = address_plus_mask(value)

def address_plus_mask(value):
    result = value
    for index,char in mask:
        result[index]=char
for line in lines:
    if line[:4] == 'mask':
        mask = line[7:]
        print(mask)
    if line[:3] == 'mem':
        address = '{:0{}b}'.format(int(line.split("]")[0][4:]),len(mask))
        value = int(line.split("=")[1].strip())
        print(address,value)
        for index,char in enumerate(mask):
            if char == '1':
                continue# value[index]='1'
            if char == '0':
                continue# value[index]='0'
        memory[address] = value

# print(memory)
# print(sum(memory.values()))