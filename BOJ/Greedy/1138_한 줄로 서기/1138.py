import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [-1 for _ in range(n)]

for i in range(n):
    jumped = 0
    cur = 0
    while ans[cur] != -1 or jumped != arr[i]:
        if ans[cur] != -1:
            cur += 1
        elif ans[cur] == -1:
            jumped += 1
            cur += 1
    
    ans[cur] = i+1

print(*ans)