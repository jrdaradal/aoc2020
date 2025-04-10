# 2020 Advent of Code Day 09 Solution
# John Roy Daradal 

# SolutionA: 27911108

import itertools 
from utils import * 

def input09(full: bool) -> tuple[int, list[int]]:
    numbers = [int(x) for x in readLines(getPath(9, full))]
    return (numbers[0], numbers[1:])

def day09A():
    full = True 
    window, numbers = input09(full)
    for i in range(window, len(numbers)):
        if not hasPairSum(numbers[i], numbers[i-window:i]):
            print(numbers[i])
            return

def hasPairSum(target: int, numbers: list[int]) -> bool:
    for p in itertools.combinations(numbers, 2):
        if sum(p) == target:
            return True
    return False

if __name__ == '__main__':
    day09A()