import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    local_max = None
    ans = 0
    buy = 0
    for i in range(n-1, -1, -1):
        if local_max == None:
            local_max = (i, arr[i])
            continue
        
        if local_max and local_max[1] <= arr[i]:
            date, price = local_max
            ans += (date - i - 1) * price - buy
            local_max = (i, arr[i])
            buy = 0
        
        elif local_max and local_max[1] > arr[i]:
            buy += arr[i]

    date, price = local_max
    ans += date * price - buy

    print(ans)

for _ in range(int(input())):
    solve()