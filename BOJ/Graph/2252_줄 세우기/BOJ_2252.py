import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

# a, b = a가 b 앞에 서야(나와야)한다 = a -> b의 간선 연결
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 방문하지 않은 점에 대해 재귀 dfs를 다 수행하고 나서 i를 reversetopo에 append
def dfs(i):
    global visited, reversetopo
    visited[i] = True
    for nxt in graph[i]:
        if not visited[nxt]:
            dfs(nxt)
    reversetopo.append(i)


visited = [False for _ in range(n+1)]
reversetopo = []
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

# reversetopo에는 topological order의 역순으로 들어가 있음
reversetopo.reverse()
print(*reversetopo)