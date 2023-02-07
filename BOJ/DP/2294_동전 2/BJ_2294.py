import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]

for i in range(k) :
    v1, v2 = map(int, input().split())
    graph[v1-1][v2-1] = 1
    graph[v2-1][v1-1] = 1

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if graph[i][k] and graph[k][j] :
                graph[i][j] = 1

print(sum(graph[0]) - 1)