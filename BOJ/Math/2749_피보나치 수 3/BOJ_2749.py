import sys
input = sys.stdin.readline

n = int(input())
d = 1000000
p = 1500000

a, b = 0, 1
for _ in range(n % p):
    a, b = b, (a + b)
    a %= d
    b %= d

print(a)