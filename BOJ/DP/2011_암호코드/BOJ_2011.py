import sys
input = sys.stdin.readline

message = list(map(int, input().rstrip()))
dp = [0 for _ in range(len(message) + 1)]
dp[0] = 1
dp[1] = 1 if message[0] != 0 else 0

for i in range(2, len(message)+1):
    if message[i-1] != 0:
        dp[i] += dp[i-1]
    
    if message[i-2] != 0 and 1 <= message[i-2] * 10 + message[i-1] <= 26:
        dp[i] += dp[i-2]

print(dp[-1] % 1000000)