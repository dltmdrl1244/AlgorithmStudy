import sys
from collections import deque
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
selected = deque([arr[i] for i in range(k)])
ans = 0

for i in range(k, n+k):
    selected.popleft()
    selected.append(arr[i % n])
    ans = max(ans, len(set(selected).union(set([c]))))

print(ans)