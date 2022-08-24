import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
maxarea = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    global arr, maxarea
    area = 1
    arr[i][j] = 0
    q = deque()
    q.append([i, j])
    
    while q:
        cury, curx = q.popleft()
        for i in range(4):
            ny = cury + dy[i]
            nx = curx + dx[i]
            
            if 0<=ny<n and 0<=nx<m and arr[ny][nx] == 1:
                arr[ny][nx] = 0
                area += 1
                q.append([ny, nx])
                
    if maxarea < area:
        maxarea = area
    

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 1 :
            bfs(i, j)
            cnt += 1

print(cnt)
print(maxarea)