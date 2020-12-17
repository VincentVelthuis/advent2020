import sys

def printgrid(list):
    for row,col in enumerate(list):
        print(row,col)

def count_trees(grid,slope_down,slope_right):
    trees_hit=0
    rows,cols=len(grid),len(grid[0])
    #cols=len(grid[0])

    for row in range(0,rows,slope_down):
        col=int(slope_right*(row/slope_down))
        #print(step,row,col)
        if grid[row][col%cols] == '#':
            trees_hit += 1
            #print(row,col,col%cols)
    return trees_hit
 
##RUN from here
grid=[] 
with open(sys.argv[1], "r") as f:
    for x,item in enumerate(f):
        grid.append([])
        for y,char in enumerate(item.strip()):   
            #print(x,y,char)
            grid[x].append(char)
t1=count_trees(grid, 1,1)
t2=count_trees(grid, 1,3)
t3=count_trees(grid, 1,5)
t4=count_trees(grid, 1,7)
t5=count_trees(grid, 2,1)

print(t1,t2,t3,t4,t5,t1*t2*t3*t4*t5)
#printgrid(grid)