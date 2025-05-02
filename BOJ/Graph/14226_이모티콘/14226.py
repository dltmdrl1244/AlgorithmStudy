import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
visited = [[False for _ in range(1001)] for _ in range(1001)]

q = deque([(1, 0)])
visited[1][0] = True

ans = 0
while q:
    for _ in range(len(q)):
        cur, board = q.popleft()

        if cur == n:
            print(ans)
            exit()

        for nxt_cur, nxt_board in [(cur, cur), (cur + board, board), (cur-1, board)]:
            if not (0 <= nxt_cur <= 1000 and 0 <= nxt_board <= 1000):
                continue

            if not visited[nxt_cur][nxt_board]:
                q.append((nxt_cur, nxt_board))
                visited[nxt_cur][nxt_board] = True

    ans += 1