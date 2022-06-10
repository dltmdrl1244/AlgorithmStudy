import sys
from math import inf
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [inf for _ in range(100001)]

for _ in range(n) :
    coins.append(int(input()))

dp[0] = 0

for coin in coins :
    dp[coin] = 1

for i in range(1, k+1) :
    for coin in coins :
        if i >= coin :
            dp[i] = min(dp[i], dp[i-coin] + 1)
            
if dp[k] == inf :
    print(-1)
else :
    print(dp[k])