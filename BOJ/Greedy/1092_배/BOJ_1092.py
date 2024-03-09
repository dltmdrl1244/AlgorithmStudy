import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
cnt = 0
ans = 0

if crane[0] < box[0]:
    print(-1)
    sys.exit()

while box:
    for c in crane:
        idx = bisect_left(box, c)
        for i in range(idx-1, -1, -1):
            if c >= box[i]:
                box.remove(box[i])
                break

    ans += 1

print(ans)