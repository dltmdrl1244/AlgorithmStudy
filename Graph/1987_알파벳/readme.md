# 문제
링크 : https://www.acmicpc.net/problem/1987
해결여부 : Yes

# 코드
```
import sys
from collections import deque
import copy
input = sys.stdin.readline

def dfs(x, y, cnt):
    global result
    if cnt > result:
        result = cnt
        
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < r and 0 <= nx < c and not check[ord(s[ny][nx]) - 65]:
            check[ord(s[ny][nx]) - 65] = True
            dfs(nx, ny, cnt + 1)
            check[ord(s[ny][nx]) - 65] = False


r, c = map(int, input().split())
s = [list(input().strip()) for _ in range(r)]

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

check = [False] * 26
check[ord(s[0][0]) - 65] = True
result = 0

dfs(0, 0, 1)
print(result)
```

# 문제 풀이
DFS와 백트래킹을 혼합해서 사용한다.
알파벳 개수만큼 리스트 `check`를 만들어서 각 알파벳을 방문하였는지 여부를 True/False로 나타낸다.

그리고 `dfs` 함수 내에서 상하좌우 인접한 칸을 살펴본 뒤 방문하지 않은 칸이면 그 다음칸으로 이동해서 재귀적으로 다시 `dfs` 함수를 호출한다. 이 때 백트래킹 기법을 이용하여 앞뒤로 `check`를 수정해주는 작업을 거친다.

매 `dfs` 함수 호출시마다 현재 `count` 값과 max 값을 비교하여 갱신해주고, 마지막에 이를 출력한다.

# 부족했던 점
처음에는 백트래킹으로 풀지 않고 단순 DFS만 사용해서 풀었는데 시간 초과가 발생하였다.

# 마무리
이미 밟고 왔던 알파벳을 다시 방문할 수 없다는 조건을 걸었으니까, 칸을 방문했는지 여부는 자동으로 커버되므로 `visited` 등의 리스트를 사용하지 않아도 된다.