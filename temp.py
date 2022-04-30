import sys
input = sys.stdin.readline
n = int(input())

stack = []
cnt = 0
row = [0] * n

def is_possible(x, y) :
    for i in range(x) :
        if row[i] == y or abs(row[i] - y) == abs(i - x) :
            return False
    return True

for i in range(n-1, -1, -1) :
    stack.append([0, i])

while len(stack) != 0 :
    popx, popy = stack.pop()
    if popx == n - 1 :
        cnt += 1
        continue
        
    row[popx] = popy
    
    for i in range(n-1, -1, -1) :
        if is_possible(popx+1, i) :
            stack.append([popx+1, i])

print(cnt)