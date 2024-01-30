import sys
input = sys.stdin.readline

def root(p):
    while p != ids[p]:
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

n, m = map(int, input().split())
ids = [i for i in range(n+1)]
size = [1 for i in range(n+1)]

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 1:
        print("YES") if connected(a, b) else print("NO")
    else:
        union(a, b)