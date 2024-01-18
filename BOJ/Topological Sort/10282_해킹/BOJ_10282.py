import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d, c = map(int ,input().split())
    graph = [[] for _ in range(n + 1)]
    dist = [sys.maxsize for _ in range(n+1)]
    heap = []
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    heapq.heappush(heap, (0, c))
    dist[c] = 0
    # 다익스트라
    while heap:
        w, n = heapq.heappop(heap)
        for nxt, wei in graph[n]:
            if dist[nxt] > wei + w:
                dist[nxt] = wei + w
                heapq.heappush(heap, (wei + w, nxt))

    cnt = 0
    ans = 0
    for i in dist:
        if i != sys.maxsize:
            cnt += 1
            ans = max(ans, i)

    print(cnt, ans)