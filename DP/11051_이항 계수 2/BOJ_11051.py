n, k = map(int, input().split())

pascal = [[1] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(len(pascal[i-1]) - 1):
        pascal[i].append(pascal[i-1][j] + pascal[i-1][j+1])
    pascal[i].append(1)

print(pascal[n][k] % 10007)