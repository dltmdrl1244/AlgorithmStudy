import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

cctv_dir = [
    [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
    [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    [[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)]],
    [[(0, 1), (0, -1), (1, 0)], [(0, 1), (0, -1), (-1, 0)], [(1, 0), (-1, 0), (0, 1)], [(1, 0), (-1, 0), (0, -1)]],
    [[(0, 1), (0, -1), (1, 0), (-1, 0)]]
]

def calc_space(boardcopy):
    global ans
    cnt = 0
    for i in range(n):
        for j in range(m):
            if boardcopy[i][j] == 0:
                cnt += 1
    
    ans = min(ans, cnt)

def recur(curIdx, b):
    if curIdx == k:
        calc_space(b)
        return
    
    cy, cx, cctv_type = cctvs[curIdx]
    
    for directions in cctv_dir[cctv_type - 1]:
        b_copy = [i[:] for i in b]
        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            while (0 <= ny < n and 0 <= nx < m) and b_copy[ny][nx] < 6:
                if not (1 <= b_copy[ny][nx] <= 5):
                    b_copy[ny][nx] = -1
                ny, nx = ny + dy, nx + dx
        
        recur(curIdx + 1, b_copy)
    


n, m = map(int, input().split())
board = []
cctvs = []
ans = sys.maxsize

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(m):
        if 0 < t[j] < 6:
            cctvs.append((i, j, t[j]))
    board.append(t)
    
k = len(cctvs)
recur(0, [b[:] for b in board])
print(ans)