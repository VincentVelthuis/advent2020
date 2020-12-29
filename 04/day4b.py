import sys
import string

correct_passports = 0
passport = {} #start with empty passport

def goodyear(data, low, upp):
    return len(data)==4 and data.isdigit() and \
        low <= int(data) <= upp

def goodheight(data):
    if data[:-2].isdigit() and data[-2:] == "cm":
        return 150 <= int(data[:-2]) <= 193
    if data[:-2].isdigit() and data[-2:] == "in":
        return 59 <= int(data[:-2]) <= 76
    return False

def goodhaircolor(data):
    #print(data,data[0],len(data),data[1:])
    return data[0]=='#' and len(data)==7 and \
        all(c in string.hexdigits for c in data[1:])

def goodeyecolor(data):
    return data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def goodpid(data):
    #print(data, len(data))
    return len(data)==9 and data.isdigit()

def checkcontent(passport):
    byr = goodyear(passport['byr'],1920,2002)
    iyr = goodyear(passport['iyr'],2010,2020)
    eyr = goodyear(passport['eyr'],2020,2030)
    hgt = goodheight(passport['hgt'])
    hcl = goodhaircolor(passport['hcl'])
    ecl = goodeyecolor(passport['ecl'])
    pid = goodpid(passport['pid'])
    return byr and iyr and eyr and hgt and hcl and ecl and pid

def check(passport):
    global correct_passports
    check_keys = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    #print(passport)
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
