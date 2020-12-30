import sys

total = 0
with open(sys.argv[1], 'r') as f:
    questions = None
    for line in f:
        line = line.strip()
        if len(line) > 0:
            if questions is None:
                # overwrite questions with first line
                questions = set(line)
            else:
                # compare older questions with current line
                for q in questions:
                    if not q in line:
                        questions.remove(q)
        else:
            print(total, len(questions), questions)
            total += len(questions)
            questions = None
print(total)