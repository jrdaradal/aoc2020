# 2020 Advent of Code Day 03 Solution
# John Roy Daradal 

# SolutionA: 

import math
from utils import *

def input03(full: bool) -> list[str]:
    lines = readLines(getPath(3, full))
    steps, width = len(lines)-1, len(lines[0])
    totalWidth = 4 * steps 
    repeat = math.ceil(totalWidth / width)
    return [x * repeat for x in lines]

def day03A():
    full = True 
    grid = input03(full)
    pos: coords = (0,0)
    count = 0
    for i in range(len(grid)-1 ):
        pos = move3R1D(pos)
        if grid[pos[0]][pos[1]] == '#':
            count += 1
    print(count)

def move3R1D(pos: coords) -> coords:
    return (pos[0]+1,pos[1]+3)

if __name__ == '__main__':
    day03A()