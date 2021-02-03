import sys,fileinput
lines = [int(line.strip()) for line in \
    fileinput.input(files=sys.argv[1])]
    
# pl = preamble_length
# default 25
pl = 25
if sys.argv[1] == 'test.txt':
    pl = 5 # 5 for test

# find invalid num in input
invalid_num = 0
for i in range(pl,len(lines)):
    l = lines[i-pl:i]
    sums_preamble = set([a+b for a in l for b in l])
    
    num = lines[i]
    if not(num in sums_preamble):
        print("invalid num =",num)
        invalid_num = num

# find contiguous set summing to invalid num
for i,n1 in enumerate(lines):
    total = n1
    for j,n2 in enumerate(lines[i+1:]):
        total += n2
        if total > invalid_num:
            break
        elif total == invalid_num:
            contiguous_set = lines[i:i+j+2]
            encryption_weakness = min(contiguous_set) + max(contiguous_set)
            
            print("cont. set =",contiguous_set)
            print("encr. weakn. =",encryption_weakness)
            
            exit()