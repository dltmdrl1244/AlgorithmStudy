import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n)]
# dp[i][j] = i개의 item을 가지고 j 무게를 가장 효율적으로 채웠을 때 무게
items = [list(map(int, input().split())) for _ in range(n)]

# 무게, 가치 순서

for i in range(n) :
    w, v = items[i]
    for j in range(1, k+1) :
        if w > j : # i번째 item의 무게가 무게제한보다 크면, [i-1][j]
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            
print(dp[-1][k])
