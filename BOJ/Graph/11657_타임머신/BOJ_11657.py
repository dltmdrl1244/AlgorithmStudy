import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dist = [sys.maxsize for _ in range(n+1)]
edges = []

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    edges.append((v1, v2, cost))

dist[1] = 0
# 1번에서 v2로 가는 데 v1를 거쳐 가는게 더 빠르다면 교체해 주는 작업을 n-1번 반복한다.
for i in range(n):
    for v1, v2, cost in edges:
        # v1을 거쳐 가야 하는데 v1로 가는 길이 아직 없다면 continue
        if dist[v1] == sys.maxsize:
            continue

        if dist[v2] > dist[v1] + cost:
            dist[v2] = dist[v1] + cost
            # 만약 n-1번 반복해도 변경이 생긴다면 음의 사이클이 발생한다는 뜻. 바로 -1 출력하고 종료
            if i == n-1:
                print("-1")
                sys.exit(0)

for d in dist[2:]:
    if d == sys.maxsize:
        print("-1")
    else:
        print(d)