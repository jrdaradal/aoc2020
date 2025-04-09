# 2020 Advent of Code Day 05 Solution
# John Roy Daradal 

# SolutionA: 890

from utils import * 

seat = tuple[list[int], list[int]]

L, R = 0, 1
mask = {'F': L, 'B': R, 'L': L, 'R': R}

def input05(full: bool) -> list[seat]:
    def convert(line: str) -> seat:
        row, col = [],[]
        for i,x in enumerate(line):
            if i < 7:
                row.append(mask[x])
            else:
                col.append(mask[x])
        return (row,col)
    return [convert(x) for x in readLines(getPath(5, full))]

def day05A():
    full = True 
    maxID = 0 
    for s in input05(full):
        maxID = max(maxID, computeID(s))
    print(maxID)

numRows, numCols = 128, 8
def computeID(s: seat) -> int:
    rows, cols = s 
    row = findBinary(rows, numRows)
    col = findBinary(cols, numCols)
    return (row*8) + col

def findBinary(sides: list[int], limit: int) -> int:
    start, end = 0, limit 
    for s in sides[:-1]:
        mid = start + ((end-start) // 2)
        if s == L:
            end = mid
        elif s == R:
            start = mid
    return start if sides[-1] == L else end-1


if __name__ == '__main__':
    day05A()