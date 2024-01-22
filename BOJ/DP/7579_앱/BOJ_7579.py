import sys
input = sys.stdin.readline

n, m = map(int, input().split())
value = list(map(int, input().split()))
cost = list(map(int, input().split()))
ans = sys.maxsize
tc = sum(cost) + 1
dp = [[0 for _ in range(tc)] for _ in range(n)]

for i in range(n):
    item_value = value[i]
    item_cost = cost[i]

    for j in range(tc):
        if j < item_cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-item_cost] + item_value)

        if dp[i][j] >= m:
            ans = min(ans, j)

print(ans)