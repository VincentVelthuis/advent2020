with open("test_input.csv", "r") as f:
    list2 = []
    for item in f: #split every line into chunks
        item_split_space=item.split(' ')
        n1 = int(item_split_space[0].split('-')[0].strip())
        n2 = int(item_split_space[0].split('-')[1].strip())
        c  = item_split_space[1].split(':')[0].strip()
        s  = item_split_space[2].strip()
        
        list2.append([n1,n2,c,s])
print(list2)