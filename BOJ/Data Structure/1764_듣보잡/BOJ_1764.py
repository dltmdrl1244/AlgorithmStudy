import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
b = set()

for _ in range(n):
    t = input().rstrip()
    a.add(t)

for _ in range(m):
    t = input().rstrip()
    b.add(t)

c = list(a.intersection(b))
c.sort()
print(len(c), *c, sep="\n")