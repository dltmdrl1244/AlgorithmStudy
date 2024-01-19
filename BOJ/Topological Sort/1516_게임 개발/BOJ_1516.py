import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
# indegree = 하위 건물 수
indegree = [0 for _ in range(n+1)]
# time = 그 건물 자체를 짓는 데 드는 시간
time = [0 for _ in range(n+1)]
# ans = time + (하위 건물들의 소요 시간을 고려한 최종 답)
ans = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
q = deque([])

for i in range(1, n+1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    for sub in info[1:len(info)-1]:
        indegree[i] += 1
        graph[sub].append(i)

# 지을 수 있게 된 건물을 큐에 넣는다.
# indegree가 0이라는 것은 하위 종속 관계가 모두 해소되어 지을 수 있게 되었다는 뜻.
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        # 하위 건물을 고려하여 ans 갱신해주고, 종속 관계를 하나 해제해 준다.
        ans[nxt] = max(ans[nxt], ans[cur] + time[cur])
        indegree[nxt] -= 1
        
        if indegree[nxt] == 0:
            q.append(nxt)

for i in range(1, n+1):
    ans[i] += time[i]

print(*ans[1:], sep="\n")