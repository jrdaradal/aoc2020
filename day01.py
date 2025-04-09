# 2020 Advent of Code Day 01 Solution
# John Roy Daradal 

# SolutionA: 997899
# SolutionB: 131248694

import itertools
from utils import * 

def input01(full: bool) -> list[int]:
    return [int(x) for x in readLines(getPath(1, full))]

def day01A():
    full = True 
    numbers = input01(full)
    find2020Combo(numbers, 2)

def day01B():
    full = True 
    numbers = input01(full)
    find2020Combo(numbers, 3)

def find2020Combo(numbers: list[int], count: int):
    for p in itertools.combinations(numbers, count):
        if sum(p) == 2020:
            prod = 1 
            for x in p: prod *= x
            print(prod)
            break
    
if __name__ == '__main__':
    day01A()
    day01B()