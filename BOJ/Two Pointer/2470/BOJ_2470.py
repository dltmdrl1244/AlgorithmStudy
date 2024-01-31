import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
left = 0
right = n - 1
ans = []
min_value = sys.maxsize

arr.sort()

while left < right:
    l, r = arr[left], arr[right]

    if abs(l + r) < min_value:
        ans = [l, r]
        min_value = abs(l + r)
    
    if l + r < 0:
        left += 1
    elif l + r > 0:
        right -= 1
    else:
        break

print(*ans)