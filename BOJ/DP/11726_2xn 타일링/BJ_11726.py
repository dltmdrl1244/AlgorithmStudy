import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 2

for i in range(3, n+1) :
    dp[i] = dp[i-1] + dp[i-2]
# dp[i], 즉 2xi 크기의 타일을 1x2 블럭, 2x1 블럭으로 채우는 경우의 수는
# dp[i-1]에서 세로로 1x2 블럭을 붙이거나
# dp[i-2]에서 가로로 2x1 블럭을 두 개 붙이거나 하는 방법이 있다
# 그 결과 dp[i] = dp[i-1] + dp[i-2] 라는 점화식이 도출되고, 피보나치 수열이 만들어진다.

print(dp[n] % 10007)