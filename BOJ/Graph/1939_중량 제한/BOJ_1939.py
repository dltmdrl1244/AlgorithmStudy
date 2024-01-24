import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
visited = [False for _ in range(n+1)]
graph = [defaultdict(int) for _ in range(n+1)]
ans = sys.maxsize

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1][v2] = max(graph[v1][v2], cost)
    graph[v2][v1] = max(graph[v2][v1], cost)
    
start, end = map(int, input().split())
visited[start] = True

for nxt in graph[start]:
    heapq.heappush(edges, (-graph[start][nxt], nxt))

while not visited[end]:
    cost, cur = heapq.heappop(edges)
    if visited[cur]:
        continue

    ans = min(ans, -cost)
    visited[cur] = True
    
    for nxt in graph[cur]:
        if not visited[nxt]:
            heapq.heappush(edges, (-graph[cur][nxt], nxt))

print(ans)