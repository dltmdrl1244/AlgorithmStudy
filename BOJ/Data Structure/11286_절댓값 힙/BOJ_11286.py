import heapq
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))