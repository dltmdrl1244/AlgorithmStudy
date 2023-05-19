import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = [0] * n
t = 0
for i in range(n):
    t += arr[i]
    s[i] = t

print(s)