# 2020 Advent of Code Day 08 Solution
# John Roy Daradal 

# SolutionA: 1744
# SolutionB: 1174

from utils import *

code = tuple[str,int]

def input08(full: bool) -> list[code]:
    def convert(line: str) -> code:
        p = line.split() 
        return (p[0], int(p[1]))
    return [convert(x) for x in readLines(getPath(8, full))]

def day08A():
    full = True 
    codes = input08(full)
    x, _ = runCodes(codes)
    print(x)

def day08B():
    full = True 
    codes = input08(full)
    for i,(cmd,_) in enumerate(codes):
        if cmd == 'nop' or cmd == 'jmp':
            codes2 = flipNopJmp(codes, i)
            x, stuck = runCodes(codes2)
            if not stuck:
                print(x)
                return

def runCodes(codes: list[code]) -> tuple[int,bool]:
    i, x = 0, 0
    done: set[int] = set() 
    numCodes = len(codes)
    while True:
        if i in done:
            return (x, True)
        if i >= numCodes:
            return (x, False)
        
        done.add(i)
        cmd, y = codes[i]
        if cmd == 'nop':
            i += 1 
        elif cmd == 'acc':
            x += y 
            i += 1
        elif cmd == 'jmp':
            i += y 

def flipNopJmp(codes: list[code], idx: int) -> list[code]:
    codes2 = codes[:]
    cmd,y = codes2[idx]
    cmd2 = 'nop' if cmd == 'jmp' else 'jmp'
    codes2[idx] = (cmd2,y)
    return codes2

if __name__ == '__main__':
    day08A()
    day08B()