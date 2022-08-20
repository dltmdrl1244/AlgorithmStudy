import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

T = int(input())
for _ in range(T):
    size = int(input())
    board = [[-1] * size for _ in range(size)]
    startx, starty = map(int, input().split())
    endx, endy = map(int, input().split())

    q = deque()
    q.append([starty, startx])
    board[starty][startx] = 0

    while q:
        cury, curx = q.popleft()
        if cury == endy and curx == endx:
            print(board[cury][curx])
            break
        for i in range(8):
            nx = dx[i] + curx
            ny = dy[i] + cury
            if 0 <= nx < size and 0 <= ny < size and board[ny][nx] == -1:
                q.append([ny, nx])
                board[ny][nx] = board[cury][curx] + 1
