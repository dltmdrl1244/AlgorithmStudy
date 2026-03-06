import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# i행 전체를 켜기 위해 필요한 스위치 수를 리턴
def check_row(i):
    cnt = 0
    for j in range(m):
        if board[i][j] == '0':
            cnt += 1

    return cnt

# 두 행이 똑같이 생겼는지를 리턴
def compare_rows(a, b):
    for i in range(m):
        if board[a][i] != board[b][i]:
            return False
    return True


board = []
for _ in range(n):
    t = list(str(input().strip()))
    board.append(t)

k = int(input())

ans = 0

if k % 2 == 0:
    for i in range(n):
        flag = True
        for j in range(m):
            if board[i][j] == '0':
                flag = False
                break
        if flag:
            ans += 1

for i in range(n):
    tmp_ans = 0
    cnt = check_row(i)

    # i행을 켤 수 있다.
    if k >= cnt and (k - cnt) % 2 == 0:
        tmp_ans = 1
        for j in range(n):
            if i == j:
                continue
            j_cnt = check_row(j)

            if cnt == j_cnt and compare_rows(i, j):
                tmp_ans += 1

    ans = max(ans, tmp_ans)

print(ans)
