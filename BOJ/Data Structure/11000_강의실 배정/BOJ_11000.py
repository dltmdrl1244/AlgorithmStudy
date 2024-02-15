import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
cur = 0
ans = 0
start = defaultdict(int)
end = defaultdict(int)
times = []

for _ in range(n):
    s, e = map(int, input().split())
    start[s] += 1
    end[e] += 1
    times += [s, e]

times = list(set(times))
times.sort()

for time in times:
    cur -= end[time]
    cur += start[time]

    ans = max(ans, cur)

print(ans)