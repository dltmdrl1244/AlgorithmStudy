import sys
input = sys.stdin.readline

n = int(input())
ans = 0
lines = [list(map(int, input().split())) for _ in range(n)]

lines.sort()
s = lines[0][0]
e = lines[0][1]
for start, end in lines:
    if start > e:
        ans += e - s
        s = start
        
    e = max(e, end)
    
ans += e - s
print(ans)