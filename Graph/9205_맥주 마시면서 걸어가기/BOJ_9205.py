import sys
from collections import deque
input = sys.stdin.readline
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(start, stores, end):
    q = deque()
    q.append(start)
    visited = [False] * len(stores)
    
    while q:
        cury, curx = q.popleft()
        if abs(cury - end[0]) + abs(curx - end[1]) <= 1000:
            return 1
        for i in range(len(stores)):
            if not visited[i] and abs(cury - stores[i][0]) + abs(curx - stores[i][1]) <= 1000:
                visited[i] = True
                q.append(stores[i])
    return 0
            

T = int(input())
for _ in range(T):
    n = int(input())
    start = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))
    if bfs(start, store, end):
        print("happy")
    else:
        print("sad")
    