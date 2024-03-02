import sys
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
s = dict()
order = []
delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]
ans = 0

for _ in range(n*n):
    i, a, b, c, d = map(int, input().split())
    order.append(i)
    s[i] = set((a, b, c, d))

# cnt = [친구 수, 빈 칸 수]
for student in order:
    temp = []
    cnt = [[[0, 0] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in delta:
                ny, nx = i + k[0], j + k[1]
                if not (0 <= ny < n and 0 <= nx < n):
                    continue
                
                if board[ny][nx] in s[student]:
                    cnt[i][j][0] += 1
                if board[ny][nx] == 0:
                    cnt[i][j][1] += 1

            temp.append((cnt[i][j][0], cnt[i][j][1], i, j))

    temp.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    for t in temp:
        y, x = t[2], t[3]
        if board[y][x] == 0:
            board[y][x] = student
            break

# 점수 세기
for i in range(n):
    for j in range(n):
        cnt = 0
        cur = board[i][j]
        for k in delta:
            ny, nx = i + k[0], j + k[1]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if board[ny][nx] in s[cur]:
                cnt += 1
        
        if cnt >= 1:
            ans += pow(10, cnt - 1)

print(ans)