import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
ans = sys.maxsize

arr.sort()
left, right = 0, 0
while left <= right and right < n:
    if arr[right] - arr[left] < m:
        right += 1
    else:
        ans = min(ans, arr[right] - arr[left])
        left += 1

print(ans)