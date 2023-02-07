n = int(input())
mylist = []

for _ in range(n) :
    mylist.append(int(input()))
    
dp = [0 for _ in range(n)]

for i in range(n) :
    dp[i] = 1
    for j in range(n) :
        if mylist[i] > mylist[j] :
            dp[i] = max(dp[j] + 1, dp[i])
                
print(n - max(dp))