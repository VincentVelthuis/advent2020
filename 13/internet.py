b0='17,x,13,19'
# b0='23,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,431,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,x,x,409,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'
buses = [x for x in b0.split(',')]

def part2(buses):
    mods = {}
    for idx, bus in enumerate(buses):
        if bus != 'x':
            print(-idx,bus)
            mods[bus] = -idx % int(bus)

    print(mods)
    iterator = 0
    increment = 1
    for bus in mods.keys():
        while iterator % int(bus) != mods[bus]:
            print(bus,iterator,increment)
            iterator += int(increment)
        increment *= int(bus)

    return iterator

print(part2(buses))