import sys
sys.setrecursionlimit(10**6)

m, n = map(int, input().split()) # 세로 m 가로 n
arr = []
dp = [[-1 for _ in range(n)] for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(m) :
    arr.append(list(map(int, input().split())))
    
def find_way(y, x) :
    if x == n-1 and y == m-1 :
        return 1
    
    if dp[y][x] != -1 :
        return dp[y][x]
    
    dp[y][x] = 0
    
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m :
            if arr[ny][nx] < arr[y][x] :
                dp[y][x] += find_way(ny, nx)

    return dp[y][x]

print(find_way(0, 0))