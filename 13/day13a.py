import sys, fileinput, math
lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]
    
time_est = int(lines[0])
waiting_time = 100**100
earliest_bus = 0

#drop unavailable buslines
busses = [int(x) for x in lines[1].split(',') if x != 'x']

for bus in busses:
    time_diff = bus * math.ceil(time_est/bus) % time_est
    if time_diff < waiting_time:
        waiting_time = time_diff
        earliest_bus = bus
        
print(earliest_bus * waiting_time) 