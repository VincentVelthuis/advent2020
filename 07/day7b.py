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
                amount = int(content[loc])
                child = "".join(content[loc+1:loc+3])
                bags_dict[bag].append({"count":amount,"type":child})
    return bags_dict

def count_sub_bags(bags_dict, bag_name):
    count = 0
    bag = bags_dict[bag_name]
    #print(bag_name, bag)
    if len(bag) == 0:
        return count
    else:
        for cur_bag in bag:
            cur_bag_count = cur_bag['count']
            count += cur_bag_count
            count += cur_bag_count * count_sub_bags(bags_dict, cur_bag["type"])   
    return count
    
def dictprint(bags_dict):
    for bag in bags_dict:
        print("\n",bag)
        for sub_bag in bags_dict[bag]:
            print(sub_bag)
        
lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]
bags_dict = input_to_dict(lines)

#dictprint(bags_dict)

print(count_sub_bags(bags_dict,"shinygold"))