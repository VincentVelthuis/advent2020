import sys, fileinput
import numpy as np
import math

instructions = [list(line.strip()) for line in fileinput.input(files=sys.argv[1])]

ship_dir = 'E'
ship = np.array([0,0])
waypoint = np.array([10,1]) #10 east, 1 north

def read(action, value):
    if action == "F":
        move_ship(value)
    elif action in ["N","E","S","W"]:
        move_waypoint(action, value)
    elif action in ["L","R"]:
        turn(action, value)

def move_ship(value):
    global ship
    ship += value * waypoint 
    
def move_waypoint(action, value):
    global waypoint
    if action == "N":
        waypoint += np.array([0,value])
    elif action == "E":
        waypoint += np.array([value,0])
    elif action == "S":
        waypoint -= np.array([0,-1*value])
    elif action == "W":
        waypoint -= np.array([-1*value,0])
    
def turn(action,value):
    # rotate B degrees counterclockwise around origin (0,0)
    # x = cos(B)*x_1 - sin(B)*y_1
    # y = sin(B)*x_1 + cos(B)*y_1
    global waypoint
    if action == "R":
        angle = -1*math.radians(value)
    elif action == "L":
        angle = math.radians(value)
    x = math.cos(angle)*waypoint[0] - math.sin(angle)*waypoint[1]
    y = math.sin(angle)*waypoint[0] + math.cos(angle)*waypoint[1]
    
    print(action,value,waypoint, np.array([round(x),round(y)]))
    waypoint = np.array([round(x),round(y)])
    # print(round(x),round(y))

print(ship,waypoint)
for instruction in instructions:
    action = instruction[0]
    value = int("".join(instruction[1:]))
    
    read(action,value)

mh_dist = np.sum(abs(ship))#abs(ship[0])+abs(ship[1])
print(ship[0],"east,",ship[1],"north: MH dist =",mh_dist)

print(ship,waypoint)    

