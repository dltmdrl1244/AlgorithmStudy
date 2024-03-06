import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[i, i] for i in arr]

for i in range(1, n):
    dp[i][0] = max(dp[i][0], dp[i-1][0] + arr[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i])

print(max(max(dp[i]) for i in range(n)))