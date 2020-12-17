import sys
#import

start_row=0
start_col=0
slope_down=1
slope_right=3
grid=[]

def printgrid(list):
    for row,col in enumerate(list):
        print(row,col)
        
with open(sys.argv[1], "r") as f:
    for x,item in enumerate(f):
        grid.append([])
        for y,char in enumerate(item.strip()):   
            #print(x,y,char)
            grid[x].append(char)

rows=len(grid)
cols=len(grid[0])

print(len(grid),"rows",len(grid[0]),"cols")
print(len(grid)/slope_down, len(grid[0]
printgrid(grid)