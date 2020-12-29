import sys

total = 0
with open(sys.argv[1], 'r') as f:
    questions = set()
    for line in f:
        line = line.strip()
        if len(line) > 0:
            for char in line:
                questions.add(char)
        else:
            total += len(questions)
            questions=set()
print(total)