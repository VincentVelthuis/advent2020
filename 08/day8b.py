import sys,fileinput
lines = [line.strip() for line in fileinput.input(files=sys.argv[1])]

def plus_min(char):
    if char == '+':
        return 1
    if char == '-':
        return -1

def perform_action(instruction):
    #acc_step,node_step = perform_action(instruction)
    
    operation = instruction[:3]
    sign = plus_min(instruction[4])
    accumulator = int(instruction[5:])
    
    if operation == 'nop':
        return 0,1
    if operation == 'acc':
        return sign*accumulator,1
    if operation == 'jmp':
        return 0,sign*accumulator

jmp_lines =[] 
for index,line in enumerate(lines):
    if "jmp" in line:
        jmp_lines.append(index)

for i in jmp_lines:
    # print("Start with jmp on index",i)
    lines_copy = lines[:]
    lines_copy[i] = "nop"+lines_copy[i][3:]
    #print(lines_copy)
    
    
    accumulator = 0
    current_node = 0
    visited_nodes = []
    while(not(current_node in visited_nodes)):
        if(current_node + 1 > len(lines_copy)):
                print(" Last line reached if index",i,"is changed")
                print(" Accumulator at program end is",accumulator)
                break
        acc_step, node_step = perform_action(lines_copy[current_node])
        
        if current_node + node_step in visited_nodes:
            #print("\tBreak for index",i,"with accumulator",accumulator)
            break
        else:
            visited_nodes.append(current_node)
            accumulator += acc_step
            current_node += node_step
            #print(current_node,len(lines_copy))
            