import sys
n = int(sys.stdin.readline())
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def is_union(n, x, y) :
    pivot = papers[y][x]
    for i in range(n) :
        for j in range(n) :
            if papers[i+y][j+x] != pivot :
                return 0
    return 1

def dq(n, x, y, target) :
    # n이 1 즉 1x1 사각형이거나, nxn 사각형이 모두 같으면, 색깔을 확인하고 같으면 1
    if n == 1 or is_union(n, x, y) :
        if papers[y][x] == target :
            return 1
        else :
            return 0
    # nxn 사각형에서 다른 색깔이 발견되면, 즉 분할해야 할 필요가 있으면 4등분함
    else :
        count = 0
        count += dq(n//2, x, y, target)
        count += dq(n//2, x+n//2, y, target)
        count += dq(n//2, x, y+n//2, target)
        count += dq(n//2, x+n//2, y+n//2, target)
        return count
    
# 흰색 색종이 수
print(dq(n, 0, 0, 0))
# 파란색 색종이 수
print(dq(n, 0, 0, 1))