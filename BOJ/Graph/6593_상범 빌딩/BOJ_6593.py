import sys
from collections import deque
input = sys.stdin.readline

d = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

def solve(h, n, m):
    board = []
    for z in range(h):
        floor = []
        for y in range(n):
            t = list(input().rstrip())
            for i in range(m):
                if t[i] == 'S':
                    sz, sy, sx = z, y, i
                    t[i] = '.'
                if t[i] == 'E':
                    ez, ey, ex = z, y, i
                    t[i] = '.'
            floor.append(t)
        board.append(floor)
        input()
    
    q = deque([])
    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
    q.append((sz, sy, sx))
    visited[sz][sy][sx] = True
    ans = 0
    while q:
        for _ in range(len(q)):
            cz, cy, cx = q.popleft()
            if (cz, cy, cx) == (ez, ey, ex):
                print("Escaped in", ans, "minute(s).")
                return
            
            for i in range(6):
                nz, ny, nx = cz + d[i][0], cy + d[i][1], cx + d[i][2]
                
                if not (0 <= nz < h and 0 <= ny < n and 0 <= nx < m):
                    continue
                if board[nz][ny][nx] != '#' and not visited[nz][ny][nx]:
                    visited[nz][ny][nx] = True
                    q.append((nz, ny, nx))

        ans += 1
    print("Trapped!")

while True:
    h, n, m = map(int, input().split())
    if (h, n, m) == (0, 0, 0):
        break
    solve(h, n, m)