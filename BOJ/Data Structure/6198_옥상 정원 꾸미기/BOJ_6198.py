import sys
input = sys.stdin.readline

n = int(input())
b = []
stack = []
ans = [0 for _ in range(n)]

for _ in range(n):
    b.append(int(input()))

stack.append(n-1)
for i in range(n-2, -1, -1):
    while stack and b[stack[-1]] < b[i]:
        ans[i] += ans[stack[-1]] + 1
        stack.pop()
    
    stack.append(i)

print(sum(ans))