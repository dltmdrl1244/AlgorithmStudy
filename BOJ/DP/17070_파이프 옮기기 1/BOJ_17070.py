import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        # 가로로 오는 케이스
        if board[i][j] == 1:
            continue
        if j > 0:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
        
        # 세로로 오는 케이스
        if i > 0:
            dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
        
        # 대각선으로 오는 케이스
        if i > 0 and j > 0 and sum([board[i][j-1], board[i-1][j]]) == 0:
            dp[i][j][2] += sum(dp[i-1][j-1])

print(sum(dp[n-1][n-1]))