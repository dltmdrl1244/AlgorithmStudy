import sys
input = sys.stdin.readline

h, w = map(int, input().split())
board = list(map(int, input().split()))
ans = 0

tmp = 0
length = 0
prev_high = 0
prev = 0
for i in range(1, w-1):
    left_max = max(board[:i])
    right_max = max(board[i+1:])

    if board[i] < min(left_max, right_max):
        ans += min(left_max, right_max) - board[i]
    
print(ans)