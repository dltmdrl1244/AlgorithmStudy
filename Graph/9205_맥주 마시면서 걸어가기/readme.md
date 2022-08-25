# 문제
링크 : https://www.acmicpc.net/problem/9205
해결여부 : Yes

# 코드
```
import sys
from collections import deque
input = sys.stdin.readline
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(start, stores, end):
    q = deque()
    q.append(start)
    visited = [False] * len(stores)
    
    while q:
        cury, curx = q.popleft()
        if abs(cury - end[0]) + abs(curx - end[1]) <= 1000:
            return 1
        for i in range(len(stores)):
            if not visited[i] and abs(cury - stores[i][0]) + abs(curx - stores[i][1]) <= 1000:
                visited[i] = True
                q.append(stores[i])
    return 0
            

T = int(input())
for _ in range(T):
    n = int(input())
    start = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))
    if bfs(start, store, end):
        print("happy")
    else:
        print("sad")
    
```

# 문제 풀이
시작점, 편의점, 도착점만 고려하였다.
먼저 시작점을 큐에 넣는다.
큐에서 꺼낸 점에서 시작해서 도착점까지 갈 수 있는지 (맨해튼 거리가 1000 이하인지) 먼저 본다. 갈 수 있다면 바로 1 리턴, `happy `출력.
그 다음에는 편의점들 중에서 갈 수 있는 편의점이 있는지 찾는다. 만약 있다면 편의점의 좌표를 큐에 넣는다. 다시 편의점에서부터 1000 거리 안에서 움직일 수 있다. 이 때 무한루프에 걸리지 않도록, 편의점 최초 방문 시 `visited `정보를 갱신해준다.
큐가 빌 때까지 도착점을 찾지 못했다면, 시작점에서든 편의점에서든 다음 편의점 또는 도착점을 찾지 못했다는 뜻이므로 0 리턴, 즉 `sad`를 출력한다.

# 마무리
모든 점을 고려하자니 좌표의 범위가 -32468~32467이라서 65535 by 65535의 엄청난 리스트를 사용해야 해서 불가능하다.
이동할 수 있는 최대 거리의 바운더리가 1000이라는 점에 착안하였다.