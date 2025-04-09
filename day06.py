# 2020 Advent of Code Day 06 Solution
# John Roy Daradal 

# SolutionA: 6763
# SolutionB: 3512

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

def day06B():
    full = True 
    total = 0 
    for g in input06(full):
        total += countAllYes(g)
    print(total)

def countYes(g: group) -> int:
    s = set()
    for x in g:
        s = s.union(set(x))
    return len(s)

def countAllYes(g: group) -> int:
    count = {}
    for x in g:
        for c in x:
            count.setdefault(c, 0)
            count[c] += 1
    return len([k for k,v in count.items() if v == len(g)])


if __name__ == '__main__':
    day06A()
    day06B()
