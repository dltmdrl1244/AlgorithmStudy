import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    coins.sort()
    m = int(input())
    dp = [0 for _ in range(m+1)]
    dp[0] = 1

    for coin in coins:
        for i in range(m+1):
            if i >= coin:
                dp[i] += dp[i-coin]

    print(dp[-1])