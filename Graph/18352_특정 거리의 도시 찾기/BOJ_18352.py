import sys
from collections import deque
input = sys.stdin.readline

v, e, k, x = map(int, input().split())
edge = [[] for _ in range(v+1)]
for _ in range(e):
    v1, v2 = map(int, input().split())
    edge[v1].append(v2)
    
def bfs(start):
    q = deque()
    q.append([start, 0])
    visited = [False] * (v+1)
    result = []

    while q:
        curv, cnt = q.popleft()
        if visited[curv]:
            continue
        if cnt == k:
            result.append(curv)
            
        visited[curv] = True
        
        for e in edge[curv]:
             q.append([e, cnt+1])
            
       
    result.sort()
    return result


result = bfs(x)
if result:
    for r in result:
        print(r)
else:
    print(-1)
