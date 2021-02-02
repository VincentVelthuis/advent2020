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
    #print("perform action:",operation,sign,accumulator)
    
    if operation == 'nop':
        return 0,1
    if operation == 'acc':
        return sign*accumulator,1
    if operation == 'jmp':
        return 0,sign*accumulator
    

accumulator = 0
current_node = 0
visited_nodes = []
#repeat=False
while(not(current_node in visited_nodes)):
    #print("\n",current_node,visited_nodes)

    acc_step, node_step = perform_action(lines[current_node])
    #print(current_node, node_step, accumulator, acc_step ,visited_nodes)
    if current_node + node_step in visited_nodes:
        print("BREAK with accumulator",accumulator)
        break;
    else:
        visited_nodes.append(current_node)
        accumulator += acc_step
        current_node += node_step