n = int(input())
m = int(input())
vip = []
dp = [1,1,2]
sum = 1

for i in range(m) :
    vip.append(int(input()))
    
for i in range(3, 41) :
    dp.append(dp[i-1] + dp[i-2])

if n <= 2 :
    sum = dp[n]
else :
    prev = 0
    for i in range(m) :
        sum *= dp[vip[i] - prev - 1]
        prev = vip[i]
    sum *= dp[n-prev]

print(sum)