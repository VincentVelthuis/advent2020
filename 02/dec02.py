import sys

valid_pws = 0

with open(sys.argv[1], "r") as f:
    for item in f: #split every line into usable chunks
        item_split_space=item.split(' ')
        n1 = int(item_split_space[0].split('-')[0].strip())
        n2 = int(item_split_space[0].split('-')[1].strip())
        c  = item_split_space[1].split(':')[0].strip()
        s  = item_split_space[2].strip()
        c_in_s = s.count(c)
        valid = n1 <= c_in_s <= n2
        
        if valid:
            valid_pws += 1

print(valid_pws)