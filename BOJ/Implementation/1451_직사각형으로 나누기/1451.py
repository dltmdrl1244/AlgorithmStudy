import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
ans = 0

for _ in range(n):
    tmp = [int(i) for i in str(input().rstrip())]
    board.append(tmp)

if n >= 3: # 가로로 두 번 자르는 경우
    for combi in combinations(range(1, n), 2):
        tmp_ans = 1
        boundary = [0] + list(combi) + [n]
        for i in range(3):
            start = boundary[i]
            end = boundary[i+1]
            tmp_count = 0
            for y in range(start, end):
                for x in range(m):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count
        
        ans = max(ans, tmp_ans)


if m >= 3: # 세로로 두 번 자르는 경우 
    for combi in combinations(range(1, m), 2):
        tmp_ans = 1
        boundary = [0] + list(combi) + [m]
        for i in range(3):
            start = boundary[i]
            end = boundary[i + 1]
            tmp_count = 0
            for x in range(start, end):
                for y in range(n):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

        ans = max(ans, tmp_ans)

if n >= 2 and m >= 2:
    for garo_idx in range(1, n): # 가로로 자를 인덱스 먼저 정함
        for sero_idx in range(1, m): # 세로로 자를 인덱스
            # 긴 사각형이 위로 오는 경우 
            tmp_ans = 1
            tmp_count = 0
            for y in range(garo_idx):
                for x in range(m):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count
            tmp_count = 0
            for y in range(garo_idx, n):
                for x in range(sero_idx):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

            tmp_count = 0
            for y in range(garo_idx, n):
                for x in range(sero_idx, m):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count
            ans = max(ans, tmp_ans)
            
            
            # 긴 사각형이 아래로 오는 경우
            tmp_ans = 1
            tmp_count = 0
            for y in range(garo_idx, n):
                for x in range(m):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

            tmp_count = 0
            for y in range(garo_idx):
                for x in range(sero_idx):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

            tmp_count = 0
            for y in range(garo_idx):
                for x in range(sero_idx, m):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

            ans = max(ans, tmp_ans)

            # 긴 사각형이 왼쪽에 오는 경우
            tmp_ans = 1
            tmp_count = 0
            for y in range(n):
                for x in range(sero_idx):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

            tmp_count = 0
            for y in range(garo_idx):
                for x in range(sero_idx, m):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

            tmp_count = 0
            for y in range(garo_idx, n):
                for x in range(sero_idx, m):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

            ans = max(ans, tmp_ans)

            # 긴 사각형이 오른쪽으로 오는 경우
            tmp_ans = 1
            tmp_count = 0
            for y in range(n):
                for x in range(sero_idx, m):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

            tmp_count = 0
            for y in range(garo_idx):
                for x in range(sero_idx):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

            tmp_count = 0
            for y in range(garo_idx, n):
                for x in range(sero_idx):
                    tmp_count += board[y][x]
            tmp_ans *= tmp_count

            ans = max(ans, tmp_ans)

print(ans)