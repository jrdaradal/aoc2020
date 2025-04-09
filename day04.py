# 2020 Advent of Code Day 04 Solution
# John Roy Daradal 

# SolutionA: 254

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

required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
def isValid(p: passport) -> bool:
    return all(k in p for k in required)

if __name__ == '__main__':
    day04A()