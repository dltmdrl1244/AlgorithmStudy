import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
rev_graph = [[] for _ in range(n+1)]
ori_graph = [[] for _ in range(n+1)]
ans = [0 for _ in  range(n+1)]

# 간선 정보를 반대 방향으로 연결한 rev_graph를 만든다.
for _ in range(m):
    v1, v2, cost = map(int, input().split())
    rev_graph[v2].append((v1, cost))
    ori_graph[v1].append((v2, cost))

# 두 그래프를 가지고 시작점 X에 대한 다익스트라 알고리즘을 수행한다.
for graph in (ori_graph, rev_graph):
    dist = [sys.maxsize for _ in range(n+1)]
    dist[x] = 0
    visited = set()

    while len(visited) != n:
        min_dist = sys.maxsize
        cur = -1
        for i in range(1, n+1):
            if dist[i] < min_dist and i not in visited:
                cur = i
                min_dist = dist[i]
        
        visited.add(cur)

        for nxt, cost in graph[cur]:
            if dist[cur] + cost < dist[nxt]:
                dist[nxt] = dist[cur] + cost
                
    # 거리 정보를 ans에 더해 준다    
    ans = [ans[i] + dist[i] for i in range(n+1)]

print(max(ans[1:]))