import sys
input = sys.stdin.readline

def bin_search(left, right):
    global ans
    if left > right:
        return
    
    mid = (left + right) // 2
    a = sum(mid // balloons[i] for i in range(n))
    if a >= m:
        ans = min(ans, mid)
        bin_search(left, mid - 1)
    else:
        bin_search(mid + 1, right)
        
n, m = map(int, input().split())
balloons = list(map(int, input().split()))
ans = sys.maxsize

bin_search(1, max(balloons) * m)
print(ans)