import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
dp = [-1 for _ in range(100001)]

for i in range(n) :
    coins.append(int(sys.stdin.readline()))
    
for coin in coins :
    dp[coin] = 1
    
for i in range(1, k+1) :
    if dp[i] == 1 :
        continue
    arr = []
    flag = 0
    
    for coin in coins :
        if coin != 0 and i > coin :
            if dp[i-coin] != -1 :
                flag = 1
                arr.append(dp[i-coin])
    if flag :
        dp[i] = min(arr) + 1
    
print(dp[k])