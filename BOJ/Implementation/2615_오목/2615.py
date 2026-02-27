import sys
input = sys.stdin.readline

def simulate(sy, sx, s):
    temp_array = []
    # 반대 방향 탐색
    py, px = sy - dir[s][0], sx - dir[s][1]
    if (0 <= py < n and 0 <= px < n) and board[py][px] == board[sy][sx]:
        return
    
    for i in range(n):
        ny, nx = sy + dir[s][0] * i, sx + dir[s][1] * i
        if not (0 <= ny < 19 and 0 <= nx < 19):
            break
        if board[ny][nx] != board[sy][sx]:
            break
        
        visited[ny][nx] |= 1 << s
        temp_array.append((ny, nx))
    
    if len(temp_array) == 5:
        print(board[sy][sx])
        print(temp_array[0][0] + 1, temp_array[0][1] + 1)
        sys.exit()

n = 19
dir = [(0, 1), (1, 0), (-1, 1), (1, 1)]
board = []
visited = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(n):
        if t[j] != 0:
            visited[i][j] = 0
            
    board.append(t)

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            for shift in range(len(dir)):
                if visited[i][j] & (1 << shift) == 0:
                    simulate(i, j, shift)

print(0)