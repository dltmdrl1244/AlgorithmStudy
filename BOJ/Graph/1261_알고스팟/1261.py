import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
def solve():
    visited = [[False for _ in range(m)] for _ in range(n)]

    q = deque([])
    visited[0][0] = True
    q.append((0, 0, 0))
    while q:
        cy, cx, cd = q.popleft()
        if (cy, cx) == (n-1, m-1):
            return cd
        
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if not (0 <= ny < n and 0 <= nx < m):
                continue
            
            if board[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.appendleft((ny, nx, cd))
            
            if board[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, cd + 1))


print(solve())