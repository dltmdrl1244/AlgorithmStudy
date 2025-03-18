import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

ids = [i for i in range(n+1)]
size = [1 for _ in range(n+1)]

def root(p):
    while ids[p] != p:
        p = ids[p]
    return p

def connected(p, q):
    return root(p) == root(q)

def union(p, q):
    a, b = root(p), root(q)
    if a == b:
        return
    
    if size[a] < size[b]:
        ids[a] = b
        size[b] += a
    else:
        ids[b] = a
        size[a] += b


for i in range(1, n+1):
    temp = list(map(int, input().split()))
    for idx, j in enumerate(temp):
        if j == 1:
            union(i, idx + 1)

plan = list(map(int, input().split()))

flag = False
for i in range(len(plan) - 1):
    cur = plan[i]
    nxt = plan[i+1]
    if not connected(cur, nxt):
        flag = True
        print("NO")
        break
 
if not flag:
    print("YES")