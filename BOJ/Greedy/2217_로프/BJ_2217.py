import sys
n = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(n)]
ans = []

ropes.sort()

for i in range(n) :
    ans.append(ropes[i] * (n-i))

print(max(ans))

# 로프 1개를 쓸 땐 1등의 1배, 2개를 쓸 땐 1,2등 해서 2등의 2배,
# 3개를 쓸 땐 1,2,3등 해서 3등의 3배... 이렇게 쓰는 것이 최선이다
# 그렇다면 로프 하중을 정렬해서 곱하는 식으로 '로프를 n개 쓸 때 최대 하중' 을 구하고, 그 중에서 최댓값을 구했다.