# 2020 Advent of Code Day 06 Solution
# John Roy Daradal 

# SolutionA: 6763

from utils import * 

group = list[str]

def input06(full: bool) -> list[group]:
    groups: list[group] = []
    curr: group = []
    for line in readLines(getPath(6, full)):
        if line == '':
            groups.append(curr)
            curr = []
        else:
            curr.append(line)
    groups.append(curr)
    return groups 

def day06A():
    full = True 
    total = 0
    for g in input06(full):
        total += countYes(g)
    print(total)

def countYes(g: group) -> int:
    s = set()
    for x in g:
        s = s.union(set(x))
    return len(s)

if __name__ == '__main__':
    day06A()
