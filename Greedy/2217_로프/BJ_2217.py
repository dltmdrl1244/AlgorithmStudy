import sys
n = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(n)]
ans = []

ropes.sort()

for i in range(n) :
    ans.append(ropes[i] * (n-i))

print(max(ans))