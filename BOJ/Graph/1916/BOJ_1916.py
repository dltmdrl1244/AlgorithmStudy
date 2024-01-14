import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dist =  [sys.maxsize for _ in range(n+1)]
visited = set()

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))

s, e = map(int, input().split())
dist[s] = 0

cur = s

while e not in visited:
    for v, c in graph[cur]:
        dist[v] = min(dist[v], dist[cur] + c)
    
    minIdx = -1
    minVal = sys.maxsize

    for i in range(1, n+1):
        if i not in visited and dist[i] < minVal:
            minIdx = i
            minVal = dist[i]
    
    visited.add(minIdx)
    cur = minIdx

print(dist[e])