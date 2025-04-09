# 2020 Advent of Code Day 04 Solution
# John Roy Daradal 

# SolutionA: 254
# SolutionB: 184

import re
from utils import * 

passport = dict[str,str]

def input04(full: bool) -> list[passport]:
    passports: list[passport] = []
    p: passport = {}
    for line in readLines(getPath(4, full)):
        if line == '':
            passports.append(p)
            p = {}
        else:
            for k,v in [x.split(':') for x in line.split()]:
                p[k] = v
    passports.append(p)
    return passports

def day04A():
    full = True 
    count = 0
    for p in input04(full):
        if isValid(p):
            count += 1 
    print(count)

def day04B():
    full = True 
    count = 0 
    for p in input04(full):
        if isFullyValid(p):
            count += 1 
    print(count)

required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
def isValid(p: passport) -> bool:
    return all(k in p for k in required)

def isFullyValid(p: passport) -> bool:
    ok = 0 
    for k, v in p.items():
        if k == 'byr':
            x = int(v)
            if len(v) == 4 and 1920 <= x and x <= 2002:
                ok += 1
        elif k == 'iyr':
            x = int(v)
            if len(v) == 4 and 2010 <= x and x <= 2020:
                ok += 1
        elif k == 'eyr':
            x = int(v)
            if len(v) == 4 and 2020 <= x and x <= 2030:
                ok += 1
        elif k == 'hgt':
            if v.endswith('cm') or v.endswith('in'):
                unit = v[-2:]
                x = int(v[:-2])
                if unit == 'cm' and 150 <= x and x <= 193:
                    ok += 1
                elif unit == 'in' and 59 <= x and x <= 76:
                    ok += 1
        elif k == 'hcl':
            pattern = r'^#[0-9a-f]{6}$'
            if re.match(pattern, v) != None:
                ok += 1
        elif k == 'ecl':
            if v in ('amb','blu','brn','gry','grn','hzl','oth'):
                ok += 1
        elif k == 'pid':
            pattern = r'^[0-9]{9}$'
            if re.match(pattern, v) != None:
                ok += 1
    return ok == len(required)

if __name__ == '__main__':
    day04A()
    day04B()