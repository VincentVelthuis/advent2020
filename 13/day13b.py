import sys, fileinput, math
lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]
busses = [x for x in lines[1].split(',')]

found = False
t = 400000000000000
while(not(found)):
    t += int(busses[0])
    found = True
    for time,bus in enumerate(busses):
        if bus != 'x':
            # print(t,time,bus,t+time)
            # print((t + time) % int(bus))
            if (t+time) % int(bus) > 0:
                # print("failed",bus,t+time)
                found = False
                break

print("found", t)