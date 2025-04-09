# 2020 Advent of Code Day 02 Solution
# John Roy Daradal 

# SolutionA: 582
# SolutionB: 729

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

    def isValidV2(self) -> bool:
        idx1, idx2 = self.min-1, self.max-1 
        count = 0 
        for idx in (idx1,idx2):
            if self.text[idx] == self.char:
                count += 1 
        return count == 1

def input02(full: bool) -> list[Password]:
    return [Password(x) for x in readLines(getPath(2, full))]

def day02A():
    full = True 
    count = 0
    for password in input02(full):
        if password.isValid():
            count += 1
    print(count)

def day02B():
    full = True 
    count = 0 
    for password in input02(full):
        if password.isValidV2():
            count += 1
    print(count)

if __name__ == '__main__':
    day02A()
    day02B()