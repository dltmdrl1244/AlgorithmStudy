from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[False for _ in range(101)] for _ in range(101)]
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cX = 2 * characterX
    cY = 2 * characterY
    iX = 2 * itemX
    iY = 2 * itemY
    answer = 0

    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*2, x2*2+1):
            for y in range(y1*2, y2*2+1):
                board[x][y] = True

    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*2+1, x2*2):
            for y in range(y1*2+1, y2*2):
                board[x][y] = False


    q = deque([(cX, cY)])
    visited = [[False for _ in range(101)] for _ in range(101)]
    visited[cX][cY] = True

    while q:
        for _ in range(len(q)):
            cx, cy = q.popleft()
            if (cx, cy) == (iX, iY):
                return answer // 2

            for dx, dy in d:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx <= 100 and 0 <= ny <= 100):
                    continue
                if board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

        answer += 1 