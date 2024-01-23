import sys
input = sys.stdin.readline

def recur(idx, weight):
    if idx > n:
        return
    if dp[idx][weight]:
        return
    dp[idx][weight] = True 
    
    recur(idx + 1, weight + weights[idx - 1])  # 무게를 더함
    recur(idx + 1, abs(weight - weights[idx - 1]))  # 무게를 뺌
    recur(idx + 1, weight)  # 추 사용X

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
# dp[i][j] = i번째 까지의 추를 이용해 j 무게를 만들 수 있는지
dp = [[False for _ in range(15001)] for _ in range(31)]

recur(0, 0)

for t in target:
    if t > 15000:
        print("N", end=" ")
    elif dp[n][t]: 
        print("Y", end=" ")
    else:
        print("N", end=" ")
print()