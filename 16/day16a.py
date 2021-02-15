import sys, fileinput

# global vars
rules={}
your_ticket = []
other_tickets = []

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

def count_invalid_tickets(r):
    count = 0
    for ticket in other_tickets:
        for num in ticket:
            if num not in r:
                count += num
    return count

convert_input()
# print(rules)
allowed_range = rules_to_range()
# print(allowed_range)
error_rate = count_invalid_tickets(allowed_range)
print("ER:",error_rate)