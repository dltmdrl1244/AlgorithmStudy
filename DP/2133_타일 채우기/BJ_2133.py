n = int(input())

dp = [0 for i in range(31)]
dp[2] = 3

for i in range(4, 31, 2):
    dp[i] = dp[2] * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j]
    dp[i] += 2
    
print(dp[n])