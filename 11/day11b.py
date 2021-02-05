import sys,fileinput
import timeit

#Set global vars (the layout, and the unchanging dimensions of the layout
seat_layout = [list(line.strip()) for line in fileinput.input(files=sys.argv[1])]
maxRow = len(seat_layout)
maxCol = len(seat_layout[0])


def count_filled_seats():
    filled_seats = 0
    for row in seat_layout:
        # print("{} # in {}".format(row.count('#'),row))
        filled_seats += row.count('#')
    return filled_seats

def directions(seat):
    adj_seats = []
    # use min and max to prevent out of bounds
    for x in range(max(seat[0]-1,0),min(maxRow,seat[0]+2)):
        for y in range(max(seat[1]-1,0),min(maxCol,seat[1]+2)):
            if (x,y) != seat:
                adj_seats.append((x-seat[0],y-seat[1]))
    return adj_seats

def content(seat):
    return seat_layout[seat[0]][seat[1]]
    
def is_floor(seat):
    return content(seat) == '.'
    
def line_of_sight(seat):
    if not is_floor(seat):
        # print(is_floor(seat),content(seat))
        for d in directions(seat):
            for m in range(1,maxRow*maxCol):
                next_seat = (seat[0]+m*d[0], seat[1]+m*d[1])
                # if next seat is in bounds
                if 0 <= next_seat[0] < maxRow and \
                    0 <= next_seat[1] < maxCol:
                    if not is_floor(next_seat):
                        print("chair at",next_seat, content(next_seat))
                        break
                    else:
                        print("floor at",next_seat, content(next_seat))
            print("next",d)
                # seat_diff = (next_seat[0]-seat[0],next_seat[1]-seat[1])
                # # while(True):
                # print(row,col,next_seat,next_seat[0],seat_diff)
                    
                
            # x_angle = x-seat[0]
            # y_angle = y-seat[1]
            # notSame = (x_angle > 0 and y_angle > 0)
            # new_coord_inBounds = (0 <= x + x_angle <= maxRow-1)\
                # and (0 <= x + x_angle <= maxCol-1) and notSame
            # print(x,y,seat_layout[x][y])
            # z=1
            # while(new_coord_inBounds):
                # new_coord = (x + z*x_angle, y + z*y_angle)
                # new_coord_inBounds = (0 <= new_coord[0] <= maxRow)\
                    # and (0 <= new_coord[1] <= maxCol)
                # print(new_coord,content(new_coord))
                # if not is_floor(seat): #layout[new_coord] == '#''L':
                    # print("seat filled")
                    # break
                # print(new_coord)
                # z+=1
    # # for direction in adj_seats:
        # # print(seat, direction)
        
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

print_layout()
# s = (3,4)
print(line_of_sight((1,4)))
print(directions((0,0)))
print(line_of_sight((0,0)))
# print(seat_layout[3][4])
# # adjacent_seats(s)
# b = check_surroundings(s,a)

# start = timeit.default_timer()
# stopSignal = False
# while(not(stopSignal)):
    # # print_layout()
    # seats_to_update = check_seats()
    # if len(seats_to_update) > 0:
        # update_seats(seats_to_update)
    # else:
        # stopSignal = True
        # print(count_filled_seats())
# stop = timeit.default_timer()
# print('Time: ', stop - start)  