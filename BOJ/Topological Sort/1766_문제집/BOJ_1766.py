import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
heap = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 선행 문제가 없는 문제들을 우선적으로 힙에 집어넣는다.
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

res = []
while heap:
    # 힙에서 뺌과 동시에 결과 배열에 추가한다.
    # 선행 문제가 모두 해결된 문제 중 번호가 가장 작은 것을 먼저 풀어야 하므로 heap을 사용한다.
    cur = heapq.heappop(heap)
    res.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        # 선행 문제가 모두 해결된 문제를 힙에 집어넣는다
        if indegree[nxt] == 0:
            heapq.heappush(heap, nxt)

print(*res)