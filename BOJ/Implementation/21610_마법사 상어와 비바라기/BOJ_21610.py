import sys
input = sys.stdin.readline

def solve(d, s):
    global clouds
    nxt_cloud = []
    tmp = []
    cloud_set = set()

    # 구름을 이동시키고 이동시킨 곳을 셋에 넣고 물을 증가시킴
    for cy, cx in clouds:
        ny, nx = cy + dir[d][0] * s, cx + dir[d][1] * s
        ny %= n
        nx %= n

        board[ny][nx] += 1
        cloud_set.add((ny, nx))
        tmp.append((ny, nx))
    
    # 물복사 (대각선 살펴봄)
    for cy, cx in tmp:
        for i in diag_dir:
            ny, nx = cy + i[0], cx + i[1]
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if board[ny][nx] != 0:
                board[cy][cx] += 1

    # 물의 양이 2이면서 셋에 존재하지 않는 칸에 구름을 만듦
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i, j) not in cloud_set:
                nxt_cloud.append((i, j))
                board[i][j] -= 2
    
    clouds = nxt_cloud[:]

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diag_dir = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for _ in range(k):
    d, s = map(int, input().split())
    solve(d-1, s)

print(sum(sum(board[i]) for i in range(n)))