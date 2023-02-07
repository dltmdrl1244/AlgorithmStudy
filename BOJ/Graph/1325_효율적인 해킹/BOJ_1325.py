import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    q = deque()
    q.append(s)
    visited = [False] * (n+1)
    visited[s] = True
    cnt = 0
    while q:
        cur = q.popleft()
        for i in com[cur]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1

    return cnt

n, m = map(int, input().split())
com = [[] for _ in range(n+1)]


for _ in range(m):
    v1, v2 = map(int, input().split())
    com[v2].append(v1)
    
result = []
for i in range(n):
    result.append(bfs(i+1))

m = max(result)
answer = [i+1 for i in range(len(result)) if result[i] == m]
print(*answer)