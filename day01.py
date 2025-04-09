# 2020 Advent of Code Day 01 Solution
# John Roy Daradal 

# SolutionA: 997899

import itertools
from utils import * 

def input01(full: bool) -> list[int]:
    return [int(x) for x in readLines(getPath(1, full))]

def day01A():
    full = True 
    numbers = input01(full)
    for p in itertools.combinations(numbers, 2):
        if sum(p) == 2020:
            print(p[0]*p[1])
            break
    
if __name__ == '__main__':
    day01A()