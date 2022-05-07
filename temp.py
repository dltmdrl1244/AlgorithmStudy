import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
stack = []
answer = []
 
for i in range(n):
    while stack and stack[-1][1] < tower[i] :
        stack.pop()
    
    if stack :
        answer.append(stack[-1][0] + 1)
    else :
        answer.append(0)
    
    stack.append([i, tower[i]])
 
print(*answer)