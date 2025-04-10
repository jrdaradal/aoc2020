# 2020 Advent of Code Day 08 Solution
# John Roy Daradal 

# SolutionA: 1744


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
    i, x = 0, 0
    done: set[int] = set()
    while True:
        if i in done:
            print(x)
            return 
        done.add(i)
        cmd, param = codes[i]
        if cmd == 'nop':
            i += 1
        elif cmd == 'acc':
            x += param 
            i += 1 
        elif cmd == 'jmp':
            i += param

if __name__ == '__main__':
    day08A()