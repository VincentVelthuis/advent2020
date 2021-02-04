import sys,fileinput

#Set global vars (the layout, and the unchanging dimensions of the layout
seat_layout = [list(line.strip()) for line in fileinput.input(files=sys.argv[1])]
layout_dim = (len(seat_layout),len(seat_layout[0]))

def count_filled_seats(layout):
    filled_seats = 0
    for row in layout:
        print("{} # in {}".format(row.count('#'),row))
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
        if adj_seat == "#":
            return False
    return True

def crowded_seats_adjacent(seat):
    count = 0
    for adj_seat in adjacent_seats(seat):
        if seat_layout[adj_seat[0]][adj_seat[1]] == "#":
            count += 1
        # print(seat,count,adj_seat)
    return count >= 4

def print_layout(layout):
    print("\nLayout:")
    for row in layout:
        print("".join(row))

def update_seats(layout):
    new_layout = layout[:]
    for x,row in enumerate(layout):
        for y,seat in enumerate(row):
            if seat == 'L' and no_occupied_seats_adjacent((x,y)):
                new_layout[x][y] = "#"
            if seat == '#' and crowded_seats_adjacent((x,y)):
                new_layout[x][y] = "L" 
        print(new_layout[x],seat_layout[x])
    # print_layout(new_layout)
    return new_layout

stopSignal = False
for i in range(3):
    print_layout(seat_layout)
    new_layout = update_seats(seat_layout)
    seat_layout = new_layout

# for x,row in enumerate(seat_layout):
    # for y,seat in enumerate(row):
        # print((x,y),adjacent_seats((x,y)))
# print(adjacent_seats((3,4)))
# print(layout_dim)