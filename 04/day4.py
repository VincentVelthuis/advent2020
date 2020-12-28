import sys

correct_passports = 0
passport = {} #start with empty passport

def check(passport):
    global correct_passports
    check_keys = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    #check_cid = {'cid'}
    if passport.keys() >= check_keys:
        correct_passports += 1

with open(sys.argv[1], 'r') as f:
    for line in f:
        if line =='\n': #line is empty, start anew
            check(passport)
            passport={} #clear passport
        else:
            keyvalue = line.split(' ')
            for item in keyvalue:
                key = item.split(':')[0]
                value = item.split(':')[1].strip()
                passport[key]=value
    print(correct_passports)
