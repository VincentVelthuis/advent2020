import sys,fileinput

def input_to_dict(lines):
    bags_dict = {}
    for line in lines:
        sentence = line.split(' ')
        bag = "".join(sentence[:2])
        bags_dict.setdefault(bag,[]) #to not get errors, every key needs to be initiated
        content = sentence[4:]
        if len(content) % 4 == 0:
            for loc in range(0, len(content),4):
                amount = content[loc]
                child = "".join(content[loc+1:loc+3])
                bags_dict[bag].append({"count":amount,"type":child})
    return bags_dict

def bag_contains_shinygold(bags_dict, bag_name):
    count = 0
    bag = bags_dict[bag_name]
    if len(bag) == 0:
        return count
    else:
        for sub_bag in bag:
            if sub_bag["type"] == "shinygold":
                count += 1
            count += bag_contains_shinygold(bags_dict, sub_bag["type"])   
    return count

### START HERE
# READ INPUT
lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]
# CONVERT INPTUT TO DICT
bags_dict = input_to_dict(lines)
# COUNT BAGS CONTAINING AT LEAST ONE SHINYGOLD BAG
count = 0
for bag in bags_dict.keys():
    if bag_contains_shinygold(bags_dict, bag) > 0:
        count += 1

print(count)
