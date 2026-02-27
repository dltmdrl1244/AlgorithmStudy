import sys
input = sys.stdin.readline

def simulate(y, x):
    global ans
    temp_count = 0
    # 행
    for d in range(n):
        if x - d < 0 or board[y][x-d] != board[y][x]:
            break
        temp_count += 1
    for d in range(1, n):
        if x + d >= n or board[y][x+d] != board[y][x]:
            break
        temp_count += 1
    
    ans = max(ans, temp_count)
    temp_count = 0
    # 열
    for d in range(n):
        if y - d < 0 or board[y-d][x] != board[y][x]:
            break
        temp_count += 1
    for d in range(1, n):
        if y + d >= n or board[y+d][x] != board[y][x]:
            break
        temp_count += 1
    
    ans = max(ans, temp_count)

ans = 0
n = int(input())
board = []
for _ in range(n):
    t = list(str(input().strip()))
    board.append(t)

for i in range(n):
    for j in range(n):
        simulate(i, j)

for i in range(n):
    for j in range(n):
        for dy, dx in [(0, 1), (1, 0)]:
            ny, nx = i + dy, j + dx
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if board[ny][nx] == board[i][j]:
                continue
            
            board[ny][nx], board[i][j] = board[i][j], board[ny][nx]
            simulate(i, j)
            simulate(ny, nx)
            board[ny][nx], board[i][j] = board[i][j], board[ny][nx]

print(ans)