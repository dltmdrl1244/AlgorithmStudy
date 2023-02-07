# 문제
링크 : 
해결여부 : 

# 코드
```
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())


def bfs(n, k):
    q = deque()
    q.append([n, 0])
    visited = [False] * 100001

    while q:
        cur, cnt = q.popleft()

        if cur == k:
            return cnt
        if cur-1 >= 0 and not visited[cur-1]:
            q.append([cur-1, cnt+1])
            visited[cur-1] = True
        if cur+1 < 100001 and not visited[cur+1]:
            q.append([cur+1, cnt+1])
            visited[cur+1] = True
        if cur*2 < 100001 and not visited[cur*2]:
            q.append([cur*2, cnt+1])
            visited[cur*2] = True

print(bfs(n, k))
```

# 문제 풀이
간단한 bfs 문제인 것 같다. n-1, n+1, n*2를 모두 큐에 넣어가면서 하나씩 확인하되, 범위를 넘는지 확인하여 indexError가 발생하지 않게끔 해 준다.

# 마무리