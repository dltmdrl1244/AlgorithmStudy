import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [False for _ in range(n+1)]
    visited[start] = True
    q = deque([])
    q.append(start)
    score = 0
    friend = 0

    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    friend += 1
        
        if friend == n-1:
            break
        score += 1

    return score + 1

n = int(input())
graph = [[] for _ in range(n+1)]
ans = [0 for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    ans[i] = bfs(i)

min_val = min(ans[1:])
min_cnt = ans.count(min_val)
result = []

for i in range(1, n+1):
    if ans[i] == min_val:
        result.append(i)

print(min_val, min_cnt)
print(*result)