import sys
input = sys.stdin.readline

# 시작점, 초기 방향, 세대 정보를 가지고 드래곤커브를 그리는 함수
def draw_curve(x, y, d, g):
    board[y][x] = True
    moves = [d]
    '''
    i세대 드래곤 커브는 i-1세대 드래곤 커브의 끝점부터 시작하여 시작점까지의 움직임을 거꾸로 + 반시계 방향으로 돌리는 움직임을 추가한다.
    예를 들어 직전 세대가 [1, 2] 두 선분으로 이루어져 있었다면 다음 세대는 [3, 2] 움직임을 더해 원점에서부터 [1, 2, 3, 2]로 움직이면 그릴 수 있다.
    [0] -> [0, 1] -> [0, 1, 2, 1] -> [0, 1, 2, 1, 2, 3, 2, 1] ... 
    '''
    for _ in range(g):
        tmp = [(moves[len(moves) - 1 - i] + 1) % 4 for i in range(len(moves))]
        moves += tmp
    
    # 원점에서부터 따라가면서 보드에 격자점을 체크한다.
    cy, cx = y, x
    for move in moves:
        ny, nx = cy + dir[move][0], cx + dir[move][1]
        board[ny][nx] = True
        cy, cx = ny, nx


board = [[False for _ in range(101)] for _ in range(101)]
ans = 0
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
n = int(input())
for _ in range(n):
    x, y, d, g = map(int, input().split())
    draw_curve(x, y, d, g)

# 사각형의 네 점이 모두 True라면 된다.
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            ans += 1
print(ans)