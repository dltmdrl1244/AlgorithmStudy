import sys

N = int(sys.stdin.readline())
dp = [[0, 0] for _ in range(91)]
dp[1] = [0, 1]

for i in range(2, N+1) :
    dp[i][0] = dp[i-1][1] + dp[i-1][0]
    dp[i][1] = dp[i-1][0]

print(sum(dp[N]))