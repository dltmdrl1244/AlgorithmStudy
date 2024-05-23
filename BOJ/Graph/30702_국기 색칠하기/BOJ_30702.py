import sys
from collections import deque
input = sys.stdin.readline

dir = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def find_area(sy, sx):
    area = []
    q = deque([])
    visited[sy][sx] = True
    q.append((sy, sx))
    area.append((sy, sx))

    while q:
        cy, cx = q.popleft()

        for dy, dx in dir:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < h and 0 <= nx < w):
                continue

            if not visited[ny][nx] and flag_a[ny][nx] == flag_a[sy][sx]:
                visited[ny][nx] = True
                area.append((ny, nx))
                q.append((ny, nx))
    
    return area

def count_area(area):
    colors = set()
    for ay, ax in area:
        colors.add((flag_b[ay][ax]))
    
    return True if len(colors) == 1 else False

h, w = map(int, input().split())

flag_a = [list(input().rstrip()) for _ in range(h)]
flag_b = [list(input().rstrip()) for _ in range(h)]

visited = [[False for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if not visited[i][j]:
            if not count_area(find_area(i, j)):
                print("NO")
                sys.exit(0)

print("YES")