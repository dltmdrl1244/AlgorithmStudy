import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n-1
ans = []
min_val = sys.maxsize

while left < right:
    t = arr[left] + arr[right]

    if min_val > abs(t):
        ans = [arr[left], arr[right]]
        min_val = abs(t)
    
    if t > 0:
        right -= 1
    elif t < 0:
        left += 1
    else:
        break

print(*ans)