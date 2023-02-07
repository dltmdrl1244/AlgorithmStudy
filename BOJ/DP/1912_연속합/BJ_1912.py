import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n) :
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))