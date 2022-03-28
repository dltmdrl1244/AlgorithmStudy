n = int(input())
dp = [0 for _ in range(1000001)]

dp[1] = 0

for i in range(1, n+1) :
    if i * 3 < 1000001 :
        if dp[i*3] == 0 or dp[i*3] > dp[i] + 1 :
            dp[i*3] = dp[i] + 1
            
    if i * 2 < 1000001 :
        if dp[i*2] == 0 or dp[i*2] > dp[i] + 1 : 
            dp[i*2] = dp[i] + 1
            
    if i + 1 < 1000001 :
        if dp[i+1] == 0 or dp[i+1] > dp[i] + 1 :
            dp[i+1] = dp[i] + 1
    

print(dp[n])