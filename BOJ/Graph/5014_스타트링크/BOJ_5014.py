from collections import deque

f, s, g, u, d = map(int, input().split())
q = deque([s])

building = [-1] * 1000001
building[s] = 0

while q:
    cur = q.popleft()
    if cur == g:
        break
    if 1 <= cur - d and building[cur-d] == -1:
        q.append(cur-d)
        building[cur-d] = building[cur]+1
    if f >= cur + u and building [cur+u] == -1:
        q.append(cur+u)
        building[cur+u] = building[cur]+1

if building[g] == -1:
    print("use the stairs")
else:
    print(building[g])