# 2020 Advent of Code Day 03 Solution
# John Roy Daradal 

# SolutionA: 257
# SolutionB: 1744787392

import math
from utils import *

def input03(full: bool, delta: coords) -> list[str]:
    lines = readLines(getPath(3, full))
    steps = numSteps(len(lines), delta[0])
    width = len(lines[0])
    totalWidth = (1+delta[1]) * steps 
    repeat = math.ceil(totalWidth / width)
    return [x * repeat for x in lines]

def day03A():
    full = True 
    delta: coords = (1,3)
    count = countSlope(full, delta)
    print(count)

def day03B():
    full = True
    product = 1
    deltas: list[coords] = [(1,1), (1,3), (1,5), (1,7), (2,1)]
    for delta in deltas:
        count = countSlope(full, delta)
        product *= count 
    print(product)

def numSteps(height: int, dy: int) -> int:
    return (height-1) // dy

def countSlope(full: bool, delta: coords) -> int:
    pos: coords = (0,0)
    grid = input03(full, delta)
    count = 0
    steps = numSteps(len(grid), delta[0])
    for i in range(steps):
        pos = move(pos, delta)
        if grid[pos[0]][pos[1]] == '#':
            count += 1
    return count

if __name__ == '__main__':
    day03A()
    day03B()