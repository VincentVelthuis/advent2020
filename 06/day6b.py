import sys

total = 0
with open(sys.argv[1], 'r') as f:
    questions = []
    answers = set()
    for line in f:
        line = line.strip()
        for char in line:
            answers.add(char)
            
        if len(line) > 0:
            questions.append(list(line))
        else:
            if len(questions) == 1:
                total += len(questions[0])
            else:
                print(answers, questions)
                for a in answers:
                    for q in questions:
                        print(a,q)
                        if not a in q:
                            break
                    total += 1
                    print(total)
            questions = []
            answers = set()
print(total)