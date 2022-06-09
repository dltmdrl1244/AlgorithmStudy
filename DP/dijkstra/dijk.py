import heapq
import sys

input = sys.stdin.readline
v, e = map(int, input().split())
INF = 9999999
visited = [False] * (v+1)
dist = [INF] * (v+1) # 시작노드에서부터 v로 가는 최소 비용
graph = [[] for _ in range(v+1)] # [v1에서][v2, v2로 가는 비용]

for _ in range(e) :
    v1, v2, cost = map(int, input().split())
    graph[v1].append((v2, cost))

def find_smallest() :
    min_val = INF
    min_idx = 0
    for i in range(1, v+1) :
        if not visited[i] and dist[i] < min_val:
            min_value = dist[i]
            min_idx = i
    return min_idx
    

def dijkstra(start):
    dist[start] = 0
    visited[start] = True
    # 시작노드의 인접한 노드들에 대해 최단거리 계산
    for i in graph[start] :
        dist[i[0]] = i[1]

    for _ in range(v-1) :
        now = find_smallest() # 최단거리 노드 찾기
        visited[now] = True
        # 해당 노드와 인접한 노드들 간의 거리 계산
        for next in graph[now]:
            new_cost = dist[now] + next[1]
            if new_cost < dist[next[0]] :
                dist[next[0]] = new_cost
    

dijkstra(1)

for i in range(1, v+1) :
    if dist[i] == INF :
        print("INF")
    else :
        print(dist[i])