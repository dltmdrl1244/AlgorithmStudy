import sys
input = sys.stdin.readline

def bin_search(left, right):
    global ans
    if left > right:
        return
    
    mid = (left + right) // 2
    cnt = 0
    for l in arr:
        cnt += l // mid
    
    if cnt >= n:
        ans = max(ans, mid)
        bin_search(mid+1, right)
    else:
        bin_search(left, mid-1)


k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
ans = 0

bin_search(1, max(arr))
print(ans)