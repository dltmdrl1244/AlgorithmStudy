import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split())) # 건물 건설비용
    seq = [[] for _ in range(n+1)] # 상위 건물 건설규칙
    dp = [0] * (n+1) # dp[i] = i번 건물을 짓는 데 필요한 최소 시간
    indegree = [0] * (n+1) # 요구되는 하위 건물 개수

    for _ in range(k):
        a, b = map(int, input().split())
        indegree[b] += 1
        seq[a].append(b)
    
    q = deque()
    for i in range(1, n+1):
        # 바로 지을 수 있는 건물은 큐에 바로 넣고, 비용도 그 건물의 건설비용이다
        if indegree[i] == 0:
            q.append(i)
            dp[i] = cost[i]
    
    while q:
        a = q.popleft() # 건설할 건물
        for nxt in seq[a]: 
            indegree[nxt] -= 1
            dp[nxt] = max(dp[a] + cost[nxt], dp[nxt]) # 다음 건물의 처리시간에 하위건물 건설시간 고려

            if indegree[nxt] == 0: # 지을 수 있게 되면 큐에 넣는다
                q.append(nxt)
    
    ans = int(input())
    print(dp[ans])
