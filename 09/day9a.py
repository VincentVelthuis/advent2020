import sys,fileinput
lines = [int(line.strip()) for line in \
    fileinput.input(files=sys.argv[1])]

# pl = preamble_length
# default 25
pl = 25
if sys.argv[1] == 'test.txt':
    pl = 5 # 5 for test

for i in range(pl,len(lines)):
    l = lines[i-pl:i]
    sums_preamble = set([a+b for a in l for b in l])
    
    if not(lines[i] in sums_preamble):
        print(lines[i],"not found")
        exit()