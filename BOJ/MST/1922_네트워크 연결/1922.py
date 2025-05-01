import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = []
ids = [i for i in range(n+1)]
size = [1 for _ in range(n+1)]


def root(p):
    while ids[p] != p:
        p = ids[p]
    return p

def union(p, q):
    a, b = root(p), root(q)

    if size[a] < size[b]:
        ids[a] = b
        size[b] += size[a]
    else:
        ids[b] = a
        size[a] += size[b]

def connected(p, q):
    return root(p) == root(q)

for _ in range(m):
    v1, v2, cost = map(int, input().split())
    if v1 == v2:
        continue

    edges.append((cost, v1, v2))


edges.sort(key = (lambda x : x[0]))
ans = 0
for cost, v1, v2 in edges:
    if connected(v1, v2):
        continue

    ans += cost
    union(v1, v2)

print(ans)