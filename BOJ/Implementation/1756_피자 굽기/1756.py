import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
stove = list(map(int, input().split()))
pizzas = deque(list(map(int, input().split())))
capacity = []

min_size = sys.maxsize
for i in range(n):
    min_size = min(min_size, stove[i])
    capacity.append(min_size)

for i in range(n-1, -1, -1):
    if capacity[i] >= pizzas[0]:
        pizzas.popleft()
        if not pizzas:
            print(i + 1)
            break

if pizzas:
    print(0)