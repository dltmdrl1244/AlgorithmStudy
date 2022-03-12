n = int(input())
arr = list(map(int, input().split()))

dp_sum = [0 for _ in range(n)]

for i in range(n) :
    dp_sum[i] = arr[i]
    for j in range(n) :
        if arr[i] > arr[j] :
            dp_sum[i] = max(dp_sum[i], dp_sum[j] + arr[i])

print(max(dp_sum[:]))