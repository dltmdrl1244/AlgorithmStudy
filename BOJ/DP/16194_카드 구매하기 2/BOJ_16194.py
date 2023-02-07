import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dp = [float('inf')] * 1001
dp[0] = 0

for i in range(1, n+1):
    for j in range(i):
        dp[i] = min(dp[i], dp[j] + cards[i-j-1])

print(dp[n])