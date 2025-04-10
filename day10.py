# 2020 Advent of Code Day 10 Solution
# John Roy Daradal 

# SolutionA: 2590

from utils import *

def input10(full: bool) -> list[int]:
    numbers = [int(x) for x in readLines(getPath(10, full))]
    numbers.append(0)
    numbers.append(max(numbers) + 3)
    return numbers 

def day10A():
    full = True 
    numbers = input10(full)
    numbers.sort()
    diffs: dict[int,int] = {}
    for i in range(1, len(numbers)):
        d = numbers[i] - numbers[i-1]
        diffs.setdefault(d, 0)
        diffs[d] += 1 
    print(diffs[1] * diffs[3])

if __name__ == '__main__':
    day10A()