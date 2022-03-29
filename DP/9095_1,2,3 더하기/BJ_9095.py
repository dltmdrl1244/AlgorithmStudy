import sys

T = int(sys.stdin.readline())
dp = [0 for _ in range(11)]
dp[1:4] = [1, 2, 4]

for i in range(4, 11) :
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T) :
    print(dp[int(sys.stdin.readline())])