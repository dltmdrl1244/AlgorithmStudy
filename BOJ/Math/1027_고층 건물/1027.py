import sys
input = sys.stdin.readline

def is_visible(idx1, idx2): # idx1이 더 앞에 있는 빌딩
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1

    b1, b2 = arr[idx1], arr[idx2]
    # 두 직선의 기울기 r : (b2 - b1) / (idx2 - idx1)
    # 직선의 방정식 : y = r(x-idx1) + b
    r = (b2 - b1) / (idx2 - idx1)

    for i in range(idx1 + 1, idx2):
        if r * (i - idx1) + b1 <= arr[i]:
            return False
    return True
    

n = int(input())
arr = list(map(int, input().split()))
ans = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if is_visible(i, j):
            ans[i] += 1

print(max(ans))