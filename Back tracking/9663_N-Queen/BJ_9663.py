import sys
input = sys.stdin.readline
n = int(input())

rows = [0] * n
cnt = 0

def is_possible(x) :
    for i in range(x) :
        if rows[i] == rows[x] or abs(rows[i] - rows[x]) == abs(i - x) :
            return False
    return True

def queen(row) :
    global cnt
    if row == n :
        cnt += 1
        return
    
    for i in range(n) :
        rows[row] = i
        if is_possible(row) :
            queen(row + 1)

queen(0)
print(cnt)