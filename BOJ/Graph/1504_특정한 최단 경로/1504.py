import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))
    graph[v2].append((v1, cost))
    
a, b = map(int, input().split())
# 1 -> a + a -> b + b -> m
# 1 -> b + b -> a + a -> m

def dijkstra(dist, start):
    dist[start] = 0
    q = [(0, start)]
    
    while q:
        distance, node = heapq.heappop(q)
        
        if dist[node] < distance:
            continue
        
        for nxt_node, nxt_distance in graph[node]:
            if dist[nxt_node] > distance + nxt_distance:
                dist[nxt_node] = distance + nxt_distance
                heapq.heappush(q, (distance + nxt_distance, nxt_node))

dist_1 = [sys.maxsize] * (n+1)
dist_a = [sys.maxsize] * (n+1)
dist_b = [sys.maxsize] * (n+1)

for dist_array, idx in [[dist_1, 1], [dist_a, a], [dist_b, b]]:
    dijkstra(dist_array, idx)
    
ans = min(dist_1[a] + dist_a[b] + dist_b[n], dist_1[b] + dist_b[a] + dist_a[n])
print(ans if dist_1[n] != sys.maxsize else -1)