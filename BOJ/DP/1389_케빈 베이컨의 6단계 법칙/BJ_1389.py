import sys
from math import inf
input = sys.stdin.readline

n, v = map(int, input().split())
graph = [[inf] * n for _ in range(n)]

for i in range(v) :
    v1, v2 = map(int, input().split())
    graph[v1-1][v2-1] = 1
    graph[v2-1][v1-1] = 1
    
for i in range(n) :
    graph[i][i] = 0

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if i == j :
                continue
            if graph[i][k] and graph[k][j] :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
idx = 0
mval = inf
for i in range(n-1, -1, -1) :
    # print(i, sum(graph[i]))
    if mval >= sum(graph[i]) :
        mval = sum(graph[i])
        idx = i
            
print(idx+1)

