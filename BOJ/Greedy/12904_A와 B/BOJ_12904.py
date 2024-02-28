import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

while len(t) > len(s):
    l = len(t)
    if t[-1] == 'B':
        t = t[:l-1]
        t = t[::-1]
    else:
        t = t[:l-1]

print(1 if s == t else 0)