import sys,fileinput

lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]

for line in lines:
    rule = line.split(' ')
    bag = rule[:2]
    contain = rule[4:]
    if len(contain) % 4 == 0:
        for content in range(0, len(contain),4):
            print(contain[content:content+3])
    else:
        print("END")
    print(bag,contain)