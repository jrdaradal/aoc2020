# 2020 Advent of Code Day 10 Solution
# John Roy Daradal 

# SolutionA: 2590
# SolutionB: 226775649501184

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

def day10B():
    full = True 
    numbers = input10(full)
    numbers.sort()
    count = {numbers[-1]: 1}
    i = len(numbers) - 2 
    while i >= 0:
        curr = numbers[i]
        valid = [x for x in numbers[i+1:i+4] if x-curr <= 3]
        count[curr] = sum(count[x] for x in valid)
        i -= 1
    print(count[numbers[0]])

if __name__ == '__main__':
    day10A()
    day10B()