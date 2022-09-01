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