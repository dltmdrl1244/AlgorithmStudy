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
        
        if 0 <= ny < r and 0 <= nx < c and not check[ord(s[ny][nx]) - 65] and not visited[ny][nx]:
            check[ord(s[ny][nx]) - 65] = True
            visited[ny][nx] = True
            dfs(nx, ny, cnt + 1)
            check[ord(s[ny][nx]) - 65] = False
            visited[ny][nx] = False


r, c = map(int, input().split())
s = [list(input().strip()) for _ in range(r)]

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

check = [False] * 26
check[ord(s[0][0]) - 65] = True
visited = [[False] * c for _ in range(r)]
result = 0

dfs(0, 0, 1)
print(result)