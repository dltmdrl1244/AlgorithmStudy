from bisect import bisect_left 
import sys
input = sys.stdin.readline
# 이진탐색
# 같은 수일 경우 왼쪽 index

n = int(input())
arr = list(map(int, input().split()))
ans = []

for i in arr:
    # i가 들어갈 위치
    k = bisect_left(ans, i)

    # 가장 큰 수면 그냥 뒤에 붙인다
    if k == len(ans):
        ans.append(i)
    else:
        ans[k] = i

print(len(ans))
