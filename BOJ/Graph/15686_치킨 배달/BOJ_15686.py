import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
ch = []
dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2:
            ch.append((i, j))
            tmp[j] = 0
    board.append(tmp)

def bfs(combi):
    # 방문 처리와 최근접 치킨집까지의 거리를 함께 처리
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    dist = 0
    for cy, cx in combi:
        board[cy][cx] = 2
        visited[cy][cx] = 0
        q.append((cy, cx))

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[cy][cx] + 1
                    # 만약 집에 도착했다면 가장 가까운 치킨집까지의 거리를 dist에 더함
                    if board[ny][nx] == 1:
                        dist += visited[ny][nx]
                    q.append((ny, nx))
    return dist


ans = float('inf')
# 전체 치킨집 중 m개의 치킨집을 선택
for combi in combinations(ch, m):
    # 각 시행의 거리 중 최솟값 갱신
    ans = min(ans, bfs(combi))

print(ans)