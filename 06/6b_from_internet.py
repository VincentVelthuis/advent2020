import fileinput

lines = [line.strip() for line in fileinput.input(files='input.txt')]

# since we are relying on the empty line
# to identify the group of people
# empty line at the end is required to count
# the last group
#lines.append('')

yes_questions = set()
all_yes = None
sum = 0
for line in lines:
    if not line:
        # if we encounter an empty line
        # count the number of question 
        # to which everyone answered YES
        print(sum, len(all_yes), all_yes)
        sum += len(all_yes)
        all_yes = None
    else:
        if all_yes is None:
            all_yes = set(line)
        else:
            all_yes = all_yes & set(line)

print(sum)