from dis import dis
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
result = 0
shark = 2
sharkExp = 0
curPos = []
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

for i in range(n):
    for j in range(n):
        if s[i][j] == 9:
            curPos = [i, j]
            s[i][j] = 0


def find_food():
    for i in range(n):
        for j in range(n):
            if 0 < s[i][j] < shark:
                return True
    return False


def bfs(initPos):
    global shark, s, curPos, sharkExp
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    q = deque()
    q.append([initPos[0], initPos[1]])
    fish = []
    minDist = float('inf')

    while q:
        curY, curX = q.popleft()
        for i in range(4):
            ny = curY + dy[i]
            nx = curX + dx[i]
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == False and s[ny][nx] <= shark:
                visited[ny][nx] = True
                q.append([ny, nx])
                distance[ny][nx] = distance[curY][curX] + 1
                
                if 0< s[ny][nx] < shark and distance[ny][nx] <= minDist:
                    minDist = distance[ny][nx]
                    fish.append([ny, nx])
    if fish:
        fish = sorted(fish, key=lambda x: (x[0], x[1]))
        return fish[0][0], fish[0][1], distance[fish[0][0]][fish[0][1]]
    else:
        return -1, -1, -1
        
while True:
    nextY, nextX, dist = bfs(curPos)
    if nextY == -1 and nextX == -1:
        break
    curPos = [nextY, nextX]
    s[nextY][nextX] = 0
    sharkExp += 1
    if sharkExp == shark:
        shark += 1
        sharkExp = 0
    result += dist

print(result)