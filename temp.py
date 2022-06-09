import sys
input = sys.stdin.readline

n = int(input())
v = int(input())
INF = 9999999
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(v) :
    v1, v2, c = map(int, input().split())
    if graph[v1][v2] > c :
        graph[v1][v2] = c
    
for i in range(1, n+1) :
    graph[i][i] = 0

for k in range(1, n+1) :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if graph[i][j] == INF :
            print("0", end=" ")
        else :
            print(graph[i][j], end=" ")
    print()