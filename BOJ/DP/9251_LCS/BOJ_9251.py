import sys
input = sys.stdin.readline

str1 = list(input().strip())
str2 = list(input().strip())
len1 = len(str1)
len2 = len(str2)

dp = [[0] * 1001 for _ in range(1001)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[len1][len2])