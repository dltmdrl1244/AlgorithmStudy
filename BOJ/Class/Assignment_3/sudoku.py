import sys

input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(9)]
blank = []

for i in range(9) :
    for j in range(9) :
        if board[i][j] == 0 :
            blank.append([i, j])

def checkRow(y, n) :
    for i in range(9) :
        if board[y][i] == n :
            return False
    return True

def checkCol(x, n) :
    for i in range(9) :
        if board[i][x] == n :
            return False
    return True

def checkSq(x, y, n) :
    baseX = x // 3
    baseY = y // 3
    for i in range(3) :
        for j in range(3) :
            if board[baseY*3 + j][baseX * 3 + i] == n :
                return False
    return True

def check(y, x, i) :
    # 행, 열, 블록 탐색 모아놓음
    if checkRow(y, i) and checkCol(x, i) and checkSq(x, y, i) :
        return True
    else :
        return False

def dfs(x) :
    # x index가 blank 개수만큼 있으면 완료했으니 출력하고 종료
    if x == len(blank) :
        for r in range(9) :
            for c in range(9) :
                print(board[r][c], end=" ")
            print()
        exit(0)
    
    # [r][c]에 들어갈 수 있는지 확인한 후 들어갈 수 있으면 넣고 재귀, 그 후 초기화
    for i in range(1, 10) :
        r = blank[x][0]
        c = blank[x][1]
        
        if check(r, c, i) :
            board[r][c] = i
            dfs(x + 1)
            board[r][c] = 0

dfs(0)
