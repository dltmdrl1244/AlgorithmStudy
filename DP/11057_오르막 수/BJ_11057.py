import sys
n = int(sys.stdin.readline())

dp = [[0 for _ in range(10)] for _ in range(n+1)]

dp[1] = [1 for _ in range(10)]

for i in range(2, n+1) :
    for j in range(10) :
        a = 0
        for k in range(j+1) :
            a += dp[i-1][k]
        dp[i][j] = a

print(sum(dp[n]) % 10007)