import sys
input = sys.stdin.readline

def calc(numbers, ops):
    result = 0
    tempNo = 1
    for i in range(n-1):
        curN, curO = numbers[i+1], ops[i]
        if curO == '+':
            result += tempNo
            tempNo = curN
        elif curO == '-':
            result += tempNo
            tempNo = -curN
        else:
            tempNo = tempNo * 10 + curN if tempNo > 0 else tempNo * 10 - curN
    
    result += tempNo
    
    if result == 0:
        print(numbers[0], end="")
        for i in range(n-1):
            print(ops[i], numbers[i+1], end="",sep="")
        print()


def search(curIdx, numbers, ops):
    if curIdx == n+1:
        calc(numbers, ops)
        return
    
    if curIdx == n:
        calc(numbers + [curIdx], ops)
        
    else:
        for op in (' ', '+', '-'):
            search(curIdx+1, numbers + [curIdx], ops + [op])
    
    
t = int(input())
for i in range(t):
    n = int(input())
    search(1, [], [])
    if i != t-1:
        print()