import sys,fileinput

#Set global vars (the layout, and the unchanging dimensions of the layout
seat_layout = [list(line.strip()) for line in fileinput.input(files=sys.argv[1])]
layout_dim = (len(seat_layout),len(seat_layout[0]))
stopSignal = False

def count_filled_seats():
    filled_seats = 0
    for row in seat_layout:
        # print("{} # in {}".format(row.count('#'),row))
        filled_seats += row.count('#')
    return filled_seats

def adjacent_seats(seat):
    adj_seats = []
    # use min and max to prevent out of bounds
    for x in range(max(seat[0]-1,0),min(layout_dim[0],seat[0]+2)):
        for y in range(max(seat[1]-1,0),min(layout_dim[1],seat[1]+2)):
            if (x,y) != seat:
                adj_seats.append((x,y))
    return adj_seats

def no_occupied_seats_adjacent(seat):
    for adj_seat in adjacent_seats(seat):
        if seat_layout[adj_seat[0]][adj_seat[1]] == "#":
            return False
    return True

def crowded_seats_adjacent(seat):
    count = 0
    for adj_seat in adjacent_seats(seat):
        if seat_layout[adj_seat[0]][adj_seat[1]] == "#":
            count += 1
        # print(seat,count,adj_seat)
    return count >= 4

def print_layout():
    print("\nLayout:")
    for row in seat_layout:
        print("".join(row))

def check_seats():
    stu = []
    for x,row in enumerate(seat_layout):
        for y,seat in enumerate(row):
            if seat == 'L' and no_occupied_seats_adjacent((x,y)):
                stu.append((x,y))
                # new_layout[x][y] = "#"
            if seat == '#' and crowded_seats_adjacent((x,y)):
                stu.append((x,y))
    return stu

def update_seats(list_of_coord):
    for coord in list_of_coord:
        if seat_layout[coord[0]][coord[1]] == 'L':
            seat_layout[coord[0]][coord[1]] = '#'
        else:
                seat_layout[coord[0]][coord[1]] = 'L'

while(not(stopSignal)):
    # print_layout()
    seats_to_update = check_seats()
    if len(seats_to_update) > 0:
        update_seats(seats_to_update)
    else:
        stopSignal = True
        print(count_filled_seats())
