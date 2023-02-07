# 문제
링크 : https://www.acmicpc.net/problem/5014
해결여부 : yes

# 코드
```
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
```

# 문제 풀이
평범한 BFS 문제인 것 같다. 올라갈 때와 내려갈 때 범위 체크만 해 주면 나머지는 특별할 것 없을 듯?? 1697번 숨바꼭질이랑 비슷하다.

# 부족했던 점

# 마무리