import sys
input = sys.stdin.readline

def roll(cmd):
    global x, y, dice
    ny, nx = y + dir[cmd][0], x + dir[cmd][1]
    
    if not (0 <= ny < n and 0 <= nx < m):
        return
    
    tmp = dice[0]
    # 동쪽
    if cmd == 0:
        dice[0] = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[3]
        dice[3] = tmp

    # 서쪽
    elif cmd == 1:
        dice[0] = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[2]
        dice[2] = tmp

    # 북쪽
    elif cmd == 2:
        dice[0] = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[4]
        dice[4] = tmp
    
    # 남쪽
    else:
        dice[0] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[5]
        dice[5] = tmp

    dice[0] = board[ny][nx] if board[ny][nx] != 0 else dice[0]
    board[ny][nx] = 0 if board[ny][nx] != 0 else dice[0]

    print(dice[1])
    x, y = nx, ny

n, m, y, x, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# bottom, top, left, right, front, back
dice = [0, 0, 0, 0, 0, 0]
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

a = list(map(int, input().split()))
for i in a:
    roll(i-1)