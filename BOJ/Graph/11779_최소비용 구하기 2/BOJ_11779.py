import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dist = [sys.maxsize for _ in range(n+1)]
visited = set()

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))
    
start, end = map(int, input().split())
path = [[] for _ in range(n+1)]
dist[start] = 0

while end not in visited:
    min_dist = sys.maxsize
    min_city = -1
    for i in range(1, n+1):
        if dist[i] < min_dist and i not in visited:
            min_dist = dist[i]
            min_city = i

    visited.add(min_city)
    
    for nxt, cost in graph[min_city]:
        if dist[nxt] > dist[min_city] + cost and nxt not in visited:
            path[nxt] = path[min_city] + [min_city]
            dist[nxt] = dist[min_city] + cost

print(dist[end])
print(len(path[end]) + 1)
print(*(path[end] + [end]))