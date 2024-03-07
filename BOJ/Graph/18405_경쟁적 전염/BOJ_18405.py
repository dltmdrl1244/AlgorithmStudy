import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
board = []
virus = []
q = []
delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(n):
        if t[j] != 0:
            q.append((t[j], (i, j)))
    board.append(t)

s, x, y = map(int, input().split())

q.sort()
q = deque(q)

for _ in range(s):
    for _ in range(len(q)):
        num, (cy, cx) = q.popleft()
        for d in delta:
            ny, nx = cy + d[0], cx + d[1]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
        
            if board[ny][nx] == 0:
                board[ny][nx] = num
                q.append((num, (ny, nx)))

print(board[x-1][y-1])