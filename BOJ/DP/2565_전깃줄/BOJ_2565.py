import sys
input = sys.stdin.readline

n = int(input())
edges = []
dp = [1 for _ in range(n)]
ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    edges.append((a, b))

edges.sort()

for i in range(1, n):
    for j in range(i):
        if edges[i][1] > edges[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))