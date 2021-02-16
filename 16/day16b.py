import sys, fileinput

# global vars
rules={}
your_ticket = []
other_tickets = []
possible_config = {}

#functions part A
def manage_flow(line, bool1, bool2, bool3):
    if 'your ticket' in line:
        return False,True,False
    elif 'nearby ticket' in line:
        return False,False,True
    else:
        return bool1,bool2,bool3
def line_to_ticket(line):
    output = []
    for num in line.strip().split(','):
        output.append(int(num))
    return output
def line_to_rule(line):
    rule_input = line.strip().split(":")
    name = rule_input[0]
    rules.setdefault(name,[])
    rule_input = rule_input[1].split(" ")
    for x in range(1,len(rule_input)):
        r = rule_input[x]
        if r != 'or':
            low = int(r.split("-")[0])
            upp = int(r.split("-")[1])
            rules[name].append([low,upp])
def convert_input():
    global rules,your_ticket,other_tickets
    rule,your,nearby = True,False,False
    for line in fileinput.input(files=sys.argv[1]):
        rule,your,nearby = manage_flow(line,rule,your,nearby)
        if len(line) > 1:
            if rule:
                line_to_rule(line)
            elif your and ',' in line:
                your_ticket = line_to_ticket(line)
            elif nearby and ',' in line:
                other_tickets.append(line_to_ticket(line))
def rules_to_range():
    output = set()
    for name in rules:
        for r in rules[name]:
            for num in range(r[0],r[1]+1):
                output.add(num)
    return output
def find_invalid_tickets(r):
    count = 0
    invalid_indices = []
    for i,ticket in enumerate(other_tickets):
        for num in ticket:
            if num not in r:
                count += num
                invalid_indices.append(i)
    return invalid_indices[::-1]
#functions part B
def drop_invalid_tickets(l):
    global other_tickets
    for i in l:
        del other_tickets[i]
def scan_valid_tickets():
    for ticket in other_tickets:
        for index, num in enumerate(ticket):
            names = possible_names(num)
            set_names(index, names)
def possible_names(num):
    output=set()
    for name in rules:
        for range in rules[name]:
            if (range[0] <= num <= range[1]):
                # output.append(1
                output.add(name)
    return output
def set_names(index,names):
    global possible_config
    possible_config.setdefault(index,set())
    old = possible_config[index]
    if len(old) > 0:
        possible_config[index] = old & names
    else:
        possible_config[index] = names
def pprint(d):
    for elem in d:
        print(elem,d[elem])
def solution_not_found():
    length=0
    for i in possible_config:
        length += len(possible_config[i])
    return length == len(possible_config)
def find_single_element():
    for i in possible_config:
        if len(i)



#main functions
convert_input()
allowed_range = rules_to_range()
drop_invalid_tickets(find_invalid_tickets(allowed_range))
scan_valid_tickets()
pprint(possible_config)

while(solution_not_found):
    name = find_single_element()
    print(possible_config)

