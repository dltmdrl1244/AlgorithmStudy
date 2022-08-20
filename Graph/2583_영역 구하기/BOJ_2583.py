import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
# m이 세로 n이 가로
paper = [[0] * n for _ in range(m)]
area = []

for _ in range(k):
    Ax, Ay, Bx, By = map(int, input().split())
    for i in range(Ax, Bx):
        for j in range(m - By, m - Ay):
            paper[j][i] = 1

def bfs(y, x):
    global paper
    area = 1
    q = deque()
    q.append([y, x])
    paper[y][x] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and paper[ny][nx] == 0:
                paper[ny][nx] = 1
                area += 1
                q.append([ny, nx])
    return area


for i in range(m):
    for j in range(n):
        if paper[i][j] == 0:
            area.append(bfs(i, j))

print(len(area))
area.sort()
for a in area:
    print(a, end=" ")
