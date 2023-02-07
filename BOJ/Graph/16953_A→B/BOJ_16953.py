from collections import deque

A, B = map(int, input().split())
q = deque()
q.append([A, 0])

flag = 0
while q:
    n, cnt = q.popleft()
    if n >= 10e9:
        continue
    if n == B:
        print(cnt + 1)
        flag = 1
        break
    q.append([n*2, cnt+1])
    q.append([int(str(n)+"1"), cnt+1])

if not flag:
    print(-1)