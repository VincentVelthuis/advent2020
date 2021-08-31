import sys,fileinput
import matplotlib.pyplot as plt
import numpy as np

nr_iterations = 6
pocket_dimension = np.array
def initialize_dimension(file):
    initial_state = [line.strip() for line in \
                        fileinput.input(files=file)]
    
    g = len(initial_state)+2*nr_iterations
    pocket_dimension = np.zeros((g,g,g))
    center = int(g/2)
    print(center)
    
    for line_number,line in enumerate(initial_state):
        for char_number, char in enumerate(line):
            if char == '#':
                z = center
                if g%2 == 0:
                    x = int(line_number + center/2 + 1)
                    y = int(char_number + center/2 + 1)
                else:
                    x = int(line_number + center - 1)
                    y = int(char_number + center - 1)
                pocket_dimension[z,x,y] = 1
    
    # print(pocket_dimension[center])
    return pocket_dimension

def update_pocket_dimension():
    dim = len(pocket_dimension)
    updated_dimension = np.zeros((dim,dim,dim))
    
    c = 7
    turned_on =  0
    turned_off = 0
    for x in range(dim):
        for y in range(dim):
            for z in range(dim):
                updated_dimension[x,y,z] = pocket_dimension[x,y,z]
                count = count_active_neighbors(x,y,z)
                if count == 3 and pocket_dimension[x,y,z] == 0:
                    print("{} turned ON".format((x-c,y-c,z-c)))
                    updated_dimension[x,y,z] = 1
                    turned_on += 1
                if pocket_dimension[x,y,z] == 1:
                    if (count == 2 or count == 3):
                        print("{} turned OFF".format((x-c,y-c,z-c)))
                        updated_dimension[x,y,z] = 0
                        turned_off += 1
                    else:
                        print("{} remains ON".format((x-c,y-c,z-c)))
        
    print("{} new on, {} new off, {} remain on".format(\
        turned_on, turned_off, np.sum(updated_dimension)-turned_on))
    return updated_dimension    

def count_active_neighbors(a,b,c):
    count = 0
    for neighbor in find_neighbors(a,b,c):
        (x,y,z) = neighbor
        if pocket_dimension[x,y,z] == 1:
            count += 1
    return count

def find_neighbors(a,b,c):
    neighbors = set()
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                x2 = max(0,min(a+x,len(pocket_dimension)-1))
                y2 = max(0,min(b+y,len(pocket_dimension)-1))
                z2 = max(0,min(c+z,len(pocket_dimension)-1))
                neighbors.add((x2,y2,z2))
    neighbors.discard((a,b,c))
    # print(len(neighbors))
    return neighbors

def plot_space(array):
    ax = plt.figure().gca(projection='3d')
    ax.voxels(array)
    plt.show()
    
pocket_dimension = initialize_dimension(sys.argv[1])

for iteration in range(nr_iterations):
    print("start iter {}, size {}".format(\
        iteration+1,np.sum(pocket_dimension)))
    updated_dimension = update_pocket_dimension()
    pocket_dimension = updated_dimension[:]
    plot_space(pocket_dimension)
    break
    print("end iter {}, size {}".format(\
        iteration+1,np.sum(pocket_dimension)))

# print(pocket_dimension)