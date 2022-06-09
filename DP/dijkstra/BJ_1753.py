import heapq
import sys

input = sys.stdin.readline
v, e = map(int, input().split())
s = int(input())
INF = 9999999
dist = [INF] * (v+1) # 시작노드에서부터 v로 가는 최소 비용
graph = [[] for _ in range(v+1)] # [v1에서][v2, v2로 가는 비용]

for _ in range(e) :
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q :
        distance, node = heapq.heappop(q)
        if distance > dist[node] :
            continue
        
        for n in graph[node] :
            new_cost = n[1] + dist[node]
            if new_cost < dist[n[0]] :
                dist[n[0]] = new_cost
                heapq.heappush(q, (new_cost, n[0]))
    

dijkstra(s)

for i in range(1, v+1) :
    if dist[i] == INF :
        print("INF")
    else :
        print(dist[i])