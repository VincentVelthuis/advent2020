import sys, fileinput
lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]

mask = ''
memory = {}

for line in lines:
    if line[:4] == 'mask':
        mask = list(line[7:])
    if line[:3] == 'mem':
        address = int(line.split("]")[0][4:])
        value = list('{:0{}b}'.format(\
            int(line.split("=")[1].strip()),len(mask)))
        for index,char in enumerate(mask):
            if char == '1':
                value[index]='1'
            if char == '0':
                value[index]='0'
        memory[address] = int("".join(value),2)

print(sum(memory.values()))