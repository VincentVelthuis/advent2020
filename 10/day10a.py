import sys,fileinput
lines = [int(line.strip()) for line in \
    fileinput.input(files=sys.argv[1])]

# add min and max voltage
lines += [ 0, max(lines)+3 ]
# change to set to sort & change back to list to iterate
lines = list(set(lines))

one_diff = 0
three_diff = 0    
for i in range(0,len(lines)-1):
    diff_to_next = lines[i+1] - lines[i]
    if diff_to_next == 1:
        one_diff += 1
    elif diff_to_next == 3:
        three_diff += 1

print("  1:",one_diff,"\n  3:",three_diff,"\n1x3:",one_diff*three_diff)
