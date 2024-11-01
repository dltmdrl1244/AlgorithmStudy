import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = [[False for _ in range(n+1)] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def dfs(start, history):
    visited[start] = True

    for nxt in graph[start]:
        result[start][nxt] = True
        for hist in history:
            result[hist][nxt] = True

        if visited[nxt]:
            for i in range(1, n+1):
                if result[nxt][i]:
                    result[start][i] = True
                    for hist in history:
                        result[hist][i] = True
        
        else:
            dfs(nxt, history + [start])


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, [])


for _ in range(int(input())):
    a, b = map(int, input().split())
    if result[a][b] == True and result[b][a] == False:
        print(-1)
    elif result[a][b] == False and result[b][a] == True:
        print(1)
    elif result[a][b] == False and result[b][a] == False:
        print(0)