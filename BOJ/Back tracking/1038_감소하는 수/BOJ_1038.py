import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

if n >= 1023:
    print(-1)
    exit()

for i in range(10):
    heapq.heappush(heap, i)

while heap:
    cur = heapq.heappop(heap)

    if n == 0:
        print(cur)

    n -= 1
    l = len(str(cur))
    m = int(list(str(cur))[0])

    for i in range(9, m, -1):
        heapq.heappush(heap, i * (10 ** l) + cur)
