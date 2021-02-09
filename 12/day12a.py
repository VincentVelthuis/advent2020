import sys, fileinput
instructions = [list(line.strip()) for line in fileinput.input(files=sys.argv[1])]

ship_dir = 'E'
coord_east = 0
coord_north = 0

def read_instruction(action, value):
    if action == "F":
        move(ship_dir, value)
    elif action in ["N","E","S","W"]:
        move(action, value)
    elif action in ["L","R"]:
        turn(action, value)

def move(action, value):
    global coord_east, coord_north
    if action == "N":
        coord_north += value
    elif action == "E":
        coord_east += value
    elif action == "S":
        coord_north -= value
    elif action == "W":
        coord_east -= value

def turn(action, value):
    global ship_dir
    
    turn_dir = 0
    if action == "R":
        turn_dir = 1
    elif action == "L":
        turn_dir = -1
    
    # counteract out of bounds by repeating direction string
    #  3 times (NESWNESWNESW) and then locate 2nd occurence
    nesw = "NESW"*3
    # index of second occurence of "ship_dir"
    index = nesw.index(ship_dir, nesw.index(ship_dir)+ 1)
    
    ship_dir = nesw[index + turn_dir * int((value/90))]
    
    
for instruction in instructions:
    action = instruction[0]
    value = int("".join(instruction[1:]))
    
    read_instruction(action,value)
    print(action,value,"--",ship_dir, coord_north, coord_east)

