import sys
input = sys.stdin.readline

N = int(input())
sche = []
dp = [0] * (N+1)

for _ in range(N) :
    sche.append(list(map(int, input().split())))

for i in range (N-1, -1, -1) :
    if i + sche[i][0] > N :
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+1], sche[i][1] + dp[i + sche[i][0]])
        
print(dp[0])
