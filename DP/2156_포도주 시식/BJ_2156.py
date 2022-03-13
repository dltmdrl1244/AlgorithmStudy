n = int(input())

sum = [0 for _ in range(10001)]
juice = [0 for _ in range(10001)]

for i in range(1, n + 1) :
    juice[i] = int(input())
    

sum[1] = juice[1]
sum[2] = juice[1] + juice[2]
sum[3] = max(juice[1]+juice[3], juice[2]+juice[3], juice[1]+juice[2])
    
for i in range(4, n + 1) :
    sum[i] = max(sum[i-2] + juice[i], sum[i-3] + juice[i-1] + juice[i], sum[i-1])

print(sum[n])