# heapq 모듈 없이 2차원 리스트로 짜 보았는데 메모리 초과가 뜬다.
# 정점 개수가 최대 10,000개 주어지는데 2차원 배열로 만들어서 메모리 초과가 뜨는 듯

import sys
v, e = map(int, sys.stdin.readline().split())
costs = [[float('inf') for _ in range(v)] for _ in range(v)]
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]

for edge in edges :
    costs[edge[0] - 1][edge[1] - 1] = edge[2]
    costs[edge[1] - 1][edge[0] - 1] = edge[2]
    
def find_min(visited, dist) :
    mindist = float('inf')
    minv = 0
    for i in range(len(dist)) :
        if dist[i] < mindist and visited[i] == False :
            minv = i
            mindist = dist[i]
    return minv
    
def prim(start, num) :
    visited = [False for _ in range(num)]
    dist = [float('inf') for _ in range(num)]
    
    dist[start] = 0
    
    for i in range(num) :
        m = find_min(visited, dist)
        visited[m] = True
        for vertex in range(num) :
            if costs[m][vertex] != float('inf') and visited[vertex] == False :
                if dist[vertex] > costs[m][vertex] :
                    dist[vertex] = costs[m][vertex]
    print(sum(dist))

prim(0, v)