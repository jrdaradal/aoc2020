# 2020 Advent of Code Day 07 Solution
# John Roy Daradal 

# SolutionA: 185
# SolutionB: 89084

from utils import * 

bagCount = tuple[str,int]
hierarchy = dict[str,list[bagCount]]

def input07(full: bool) -> hierarchy:
    h: hierarchy = {}
    for line in readLines(getPath(7, full)):
        k,v = [x.strip() for x in line.split('contain')]
        if v == 'no other bags.':
            continue
        h[color(k)] = [newBagCount(x.strip()) for x in v.split(',')]
    return h

def day07A():
    full = True 
    h = input07(full)
    p = createParents(h)
    valid = set()
    queue = p['shiny gold']
    while len(queue) > 0:
        x = queue.pop()
        valid.add(x)
        n = p.get(x, [])
        if len(n) > 0:
            queue.extend(n)
    print(len(valid))

def day07B():
    full = True 
    h = input07(full)
    print(countInside('shiny gold', h))
        
def color(text: str) -> str:
    return ' '.join(text.split()[:-1])

def newBagCount(text: str) -> bagCount:
    p = text.split()
    return (' '.join(p[1:-1]), int(p[0]))

def createParents(h: hierarchy) -> dict[str,list[str]]:
    p: dict[str,list[str]] = {}
    for k,v in h.items():
        for color, _ in v:
            p.setdefault(color, [])
            p[color].append(k)
    return p

def countInside(color: str, h: hierarchy) -> int:
    if color in h:
        total = 0
        for color2,freq in h[color]:
            total += freq + (freq * countInside(color2, h))
        return total
    else:
        return 0

if __name__ == '__main__':
    day07A()
    day07B()