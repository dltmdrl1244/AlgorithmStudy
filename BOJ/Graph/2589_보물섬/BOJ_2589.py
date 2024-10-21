import sys
from collections import deque
input = sys.stdin.readline

def bfs(sy, sx):
    global ans
    visited[sy][sx] = True
    q.append((sy, sx))
    tmp_ans = 0

    while q:
        for _ in range(len(q)):
            cy, cx = q.popleft()
            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if board[ny][nx] == 'L' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        q.append((ny, nx))

        tmp_ans += 1
    
    ans = max(ans, tmp_ans - 1)

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
q = deque([])
ans = 0

visited = [[False for _ in range(m)] for _ in  range(n)]
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            # 가지치기 조건
            if 0 < i < n - 1:
                if board[i - 1][j] == board[i + 1][j] == 'L':
                    continue
            if 0 < j < m - 1:
                if board[i][j - 1] == board[i][j + 1] == 'L':
                    continue
            
            bfs(i, j)
            visited = [[False for _ in range(m)] for _ in  range(n)]

print(ans)