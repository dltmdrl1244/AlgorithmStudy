import sys
input = sys.stdin.readline

h, w = map(int, input().split())
c = int(input())
dolls = list(map(int, input().split()))

board = [set() for _ in range(w)]
set_idx = 0
doll_idx = 0
first_failure_index = -1
dolls.sort(reverse=True)

while doll_idx < len(dolls):
    doll = dolls[doll_idx]
    if len(board[set_idx]) < h:
        board[set_idx].add(doll)
        doll_idx += 1
        first_failure_index = -1
    
    else:
        if first_failure_index == -1:
            first_failure_index = set_idx
        else:
            if first_failure_index == set_idx:
                break
        
    set_idx = (set_idx + 1) % w

print(sum(len(board[i]) for i in range(w)))