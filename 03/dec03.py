import sys
#import

slope_right=3
trees_hit=0
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

for row in range(rows):
    col=slope_right*row
    if grid[row][col%cols] == '#':
        trees_hit += 1
    #print(row,col,grid[row][col%cols],trees_hit)

#printgrid(grid)
print(trees_hit)