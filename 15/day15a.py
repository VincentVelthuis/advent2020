# numbers = [0,3,6]
numbers = [0,3,1,6,7,5]
visited = set(numbers[:-1])

def index_of_latest(num):
    for index,item in enumerate(numbers[:-1][::-1]):
        if item == num:
            return index + 1          
    
for number in range(len(numbers),2020):
    last = numbers[-1]
    if last not in visited:
        numbers.append(0)
        visited.add(last)
    else:
        index = index_of_latest(last)
        numbers.append(index)

print(numbers[-1])#,len(numbers),numbers)