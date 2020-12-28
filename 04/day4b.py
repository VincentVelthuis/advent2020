import sys

correct_passports = 0
passport = {} #start with empty passport

def goodyear(data, low, upp):
    return len(data)==4 and data.isdigit() and \
        low <= int(data) <= upp

def goodheight(data):
    return True

def checkcontent(passport):
    byr = goodyear(passport['byr'],1920,2002)
    iyr = goodyear(passport['iyr'],2010,2020)
    eyr = goodyear(passport['eyr'],2020,2030)
    
    return byr and iyr and eyr

def check(passport):
    global correct_passports
    check_keys = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    print(passport)
    if passport.keys() >= check_keys:
        if checkcontent(passport):
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
