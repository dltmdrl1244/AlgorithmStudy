import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def bfs(group): # 같은 그룹끼리 이웃할 수 있는지 판별. 첫 도시에서 이웃한 그룹 내 도시들의 수를 리턴
    s = set(group)
    visited = [False for _ in range(n+1)]
    q = deque([group[0]])
    visited[group[0]] = True
    cnt = 0
    
    while q:
        cur = q.popleft()
        cnt += 1
        for nxt in graph[cur]:
            if not visited[nxt] and nxt in s:
                visited[nxt] = True
                q.append(nxt)

    return cnt

def find_union(s):
    global visited
    visited[s] = True
    q = deque([s])

    while q:
        c = q.popleft()
        for nxt in graph[c]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    

n = int(input())
pop = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
ans = sys.maxsize

for a in range(1, n+1):
    t = list(map(int, input().split()))
    for j in range(1, len(t)):
        b = t[j]
        graph[a].append(b)
        graph[b].append(a)

visited = [False for _ in range(n+1)]
bfs_count = 0
for i in range(1, n+1):
    if not visited[i]:
        find_union(i)
        bfs_count += 1
        
if bfs_count > 2: # 나뉜 구역이 3개 이상이면, 2개의 선거구로 나눌 수 없음
    print(-1)
    exit(0)

for count in range(1, n // 2 + 1):
    for combi in combinations(range(1, n+1), count):
        group1 = list(combi)
        group2 = [i for i in range(1, n+1) if i not in group1]
        if len(group1) == bfs(group1) and len(group2) == bfs(group2):
            a = sum(pop[i] for i in group1)
            b = sum(pop[i] for i in group2)
            ans = min(ans, abs(a - b))
    
print(ans)