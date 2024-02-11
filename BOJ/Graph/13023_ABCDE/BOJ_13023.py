import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start, d):
    global ans
    visited[start] = True
    
    if d == 5:
        ans = True
        return
    
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(nxt, d+1)

    visited[start] = False

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
ans = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    dfs(i, 1)

print(1 if ans else 0)