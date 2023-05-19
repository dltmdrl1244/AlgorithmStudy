import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(start):
    global ans
    visited[start] = True
    cycle.append(start)

    nxt = arr[start]
    
    if visited[nxt]:
        if nxt in cycle:
            ans += cycle[cycle.index(nxt):]
        
    else:
        dfs(nxt)

for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    ans = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(ans))