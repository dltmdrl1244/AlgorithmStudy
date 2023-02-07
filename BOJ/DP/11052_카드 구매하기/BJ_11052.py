n = int(input())

sum = [0 for _ in range(1001)]
price = list(map(int, input().split()))
price.insert(0, 0)
    
sum[1] = price[1]

for i in range(2, n+1) : # i개의 카드를 살 때의 최대 가격
    temp = []
    for j in range(i) :
        temp.append(sum[j] + price[i-j])
    sum[i] = max(temp)
    temp = []
    
print(sum[n])