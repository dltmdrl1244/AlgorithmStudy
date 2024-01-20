import sys
import math
input = sys.stdin.readline

def get_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))

def root(p):
    while ids[p] != p:
        p = ids[p]
    return p

def connected(p, q):
    return root(p) == root(q)

def union(p, q):
    if connected(p, q):
        return

    a, b = root(p), root(q)
    if size[a] <= size[b]:
        ids[a] = b
        size[b] += size[a]
    else:
        ids[b] = a
        size[a] += size[b]

n = int(input())
coord = []
edges = []
ids = [i for i in range(n)]
size = [1 for _ in range(n)]
ans = 0

# 좌표 저장
for i in range(n):
    x, y = map(float, input().split())
    coord.append((x, y))

for i in range(n):
    for j in range(i+1, n):
        edges.append((i, j, get_dist(coord[i], coord[j])))

edges.sort(key = lambda x: x[2])

# 비용이 적은 간선 순서대로 살펴보면서 두 정점이 서로 연결되지 않으면 서로 연결한다.
for p1, p2, dist in edges:
    if not connected(p1, p2):
        union(p1, p2)
        ans += dist

print(round(ans, 2))