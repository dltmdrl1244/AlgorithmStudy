# 문제
링크 : https://www.acmicpc.net/problem/16234
해결여부 : No

# 코드
```
from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def bfs(y, x):
    global visited
    q = deque()
    q.append([y, x])
    visited[y][x] = True
    tmp = [[y, x]]
    
    while q:
        cury, curx = q.popleft()
        for i in range(4):
            ny = cury + dy[i]
            nx = curx + dx[i]
            
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                if l<=abs(s[cury][curx] - s[ny][nx])<=r:
                    visited[ny][nx] = True
                    q.append([ny, nx])
                    tmp.append([ny, nx])
    return tmp

result = 0

while True:
    flag = 0
    tempnum = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                countries = bfs(i, j)
                if len(countries) > 1:
                    flag = 1    
                    tempnum = sum(s[y][x] for y, x in countries)
                    for y, x in countries:
                        s[y][x] = tempnum // len(countries)
    if not flag:
        break
    result += 1
    print(s)

print(result)
```

# 문제 풀이
BFS로 탐색하되, 같은 날짜에 여러 군데에서 동시다발적으로 인구이동이 일어날 수 있으므로 `bfs`를 호출할 때마다 카운트를 늘리면 안 되고 2중 for문 한 루프가 끝날 때마다 돌려야 한다. 그리고 인구이동이 단 한 군데에서도 발생하지 않았다면 `flag`가 0이 되어 종료한다.

또 한가지 주의할 점은 이미 한번 이동이 일어나서 `visited` 값이 True가 된 칸이라고 해도, 인구수가 바뀌기 때문에 이전에는 인구이동 대상이 아니었던 인접 칸과도 인구이동이 가능해질 수 있으므로 `visited` 리스트를 매 루프마다 새롭게 `false`로 초기화 해주어야 한다는 점이다. 

방문하지 않은 나라를 발견하면 `bfs` 함수를 호출하여 그 나라와 인구이동을 하는 나라들을 모두 한 리스트에 담아서 리턴 받는다. 그리고 인구수를 모두 더해서 똑같이 나눈다.

# 부족했던 점
두 가지 어려운 점이 있었는데 첫 번째는 동시에 여러 군데에서 인구이동이 일어나는 것을 어떻게 고려해야 할 것인지였다. 무한루프문의 사용과 `result` 값을 늘려주는 부분을 수정하여 해결하였다.

두 번째는 한 번 인구이동이 일어난 나라의 재인구이동인데, `visited` 리스트를 초기화시키지 않고 사용하였던 것이 문제였다. `visited`를 안 쓰자니 무한루프에 빠지고, 쓰자니 재방문을 케어할 수 없었는데 매 번 초기화 해주면 되는 문제였다.

# 마무리
`몇 번 도는가` 에 대해서 `visited` 값을 매번 초기화해주는 문제를 풀어보지 못해서 생각이 짧았었다..