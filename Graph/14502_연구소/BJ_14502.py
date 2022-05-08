# 백트래킹과 bfs를 이용하여 풀었다.
# 처음에 벽을 세우는 경우의 수를 생각해 보았는데 '설마 0인 곳에 모두 세워보고 최댓값 도출해야하나...' 생각이 들었는데 일단 해보기로 했다. 
# 백트래킹으로 벽을 세울 수 있는 경우의 수를 모두 찾고 -> 각 케이스마다 바이러스를 퍼뜨려 보고 -> 빈 칸 개수를 세서 최댓값을 갱신해준다.
# python3으로 제출하니까 시간 초과가 나서 pypy3으로 제출하니까 정답이 나오긴 했는데, 좀 더 좋은 방법이 없을까 하여 생각을 해 보다가, '벽 또는 바이러스와 인접하고 있지 않은, 그냥 쌩 바닥에다가 벽을 박는 일이 있을까?' 라는 생각을 했다. 벽을 세우는 목적이 벽을 연장하거나 바이러스를 막는 것이니...
# 그래서 0인 칸 기준으로 8방향을 탐색해서 1 또는 2가 있는지 체크하고, flag에 걸리지 않은 칸은 continue하도록 구현하였더니 3850ms에서 1850ms로 대폭 감소했다. 그래도 python3으로는 여전히 시간초과가 뜬다... 

import sys
import copy
from collections import deque

input =sys.stdin.readline
n, m = map(int, input().split()) # 세로 n 가로 m
lab = [list(map(int, input().split())) for _ in range(n)]
answer = 0
q = deque()

def bfs() :
    global answer
    cnt = 0
    arr = copy.deepcopy(lab)
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 2 :
                q.append([i, j])
               
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0] 
    
    while q :
        v = q.popleft()
        for i in range(4) :
            ny = v[0] + dy[i]
            nx = v[1] + dx[i]
            if 0 <= nx < m and 0 <= ny < n :
                if arr[ny][nx] == 0 :
                    q.append([ny, nx])
                    arr[ny][nx] = 2
    
    for line in arr :
        cnt += line.count(0)
    
    answer = max(answer, cnt)
        
def makewall(wallcount) :
    if wallcount == 3 :
        bfs()
        return
    
    else :
        dx = [-1, 0, 1, 1, 1, 0, -1, -1]
        dy = [-1, -1, -1, 0, 1, 1, 1, 0]
        
        for i in range(n) :
            for j in range(m) :
                if lab[i][j] == 0 :
                    flag = 0
                    for a in range(8) :
                        ny = i + dy[a]
                        nx = j + dx[a]
                        
                        if 0 <= ny < n and 0 <= nx < m :
                            if lab[ny][nx] in (1, 2) :
                                flag = 1
                                break
                        
                    if flag :
                        lab[i][j] = 1
                        makewall(wallcount + 1)
                        lab[i][j] = 0
    
makewall(0)
print(answer)