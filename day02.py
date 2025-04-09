# 2020 Advent of Code Day 02 Solution
# John Roy Daradal 

# SolutionA: 582

from utils import * 

class Password:
    def __init__(self, line:str):
        p = line.split(':')
        self.text = p[1].strip()
        p = p[0].strip().split()
        self.char = p[1]
        self.min, self.max = [int(x) for x in p[0].split('-')]
    
    def isValid(self) -> bool:
        count = 0 
        for char in self.text:
            if char == self.char:
                count += 1 
        return self.min <= count and count <= self.max

def input02(full: bool) -> list[Password]:
    return [Password(x) for x in readLines(getPath(2, full))]

def day02A():
    full = True 
    count = 0
    for password in input02(full):
        if password.isValid():
            count += 1
    print(count)

if __name__ == '__main__':
    day02A()