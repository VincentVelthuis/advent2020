import sys
#FBFBBFFRLR = row 44, column 5
#0101100 (F=0,B=1), 101 (R=1,L=0)
#lowest seat = 0 ( 0*8 + 0)
#highest seat = 1023 (127*8 + 7)

def convert_to_int(string):
    string = string.replace("F",'0')
    string = string.replace("B",'1')
    string = string.replace("R",'1')
    string = string.replace("L",'0')
    return int(string,2)

filled_seats=[]
with open(sys.argv[1], 'r') as f:
    for line in f:
        row = convert_to_int(line[:7])
        seat = convert_to_int(line[7:])
        seat_id = row * 8 + seat
        filled_seats.append(seat_id)
        
possible_seats = [ i for i in \
    range(min(filled_seats),max(filled_seats)+1)]
    
for i in filled_seats:
    possible_seats.remove(i)

print(max(filled_seats),possible_seats)
#print(filled_seats, min(filled_seats), max(filled_seats),possible_seats)