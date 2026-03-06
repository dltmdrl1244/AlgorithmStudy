import sys
input = sys.stdin.readline

'''
dp[i] = i개의 대포알로 만들 수 있는 사면체 최소 개수
'''


n = int(input())
tetras = [1]
arr = [1]
dp = [sys.maxsize for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1

while tetras[-1] < 300000:
    arr.append(arr[-1] + len(arr) + 1)
    tetras.append(sum(arr))


for tetra in tetras:
    for i in range(tetra, n+1):
        dp[i] = min(dp[i], dp[i-tetra] + 1)

print(dp[n])