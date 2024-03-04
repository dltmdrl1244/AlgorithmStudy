import sys
input = sys.stdin.readline

str_a = list(input().rstrip())
str_b = list(input().rstrip())
a, b = len(str_a), len(str_b)
lcs = [[0 for _ in range(b+1)] for _ in range(a+1)]
ans = 0

for i in range(1, a+1):
    for j in range(1, b+1):
        if str_a[i-1] == str_b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
            ans = max(ans, lcs[i][j])

print(ans)
