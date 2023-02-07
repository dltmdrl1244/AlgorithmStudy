n = int(input())
dp = [float('inf')] * 1000001

dp[1] = 0

def recur(n):
    print(n, end=" ")
    if dp[n-1] == dp[n] - 1:
        recur(n-1)
    elif n % 3 == 0 and dp[n//3] == dp[n] - 1:
        recur(n//3)
    elif n % 2 == 0 and dp[n//2] == dp[n] - 1:
        recur(n//2)


for i in range(2, n+1):
    dp[i] = min(dp[i-1] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3] + 1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i])
        
print(dp[n])
recur(n)