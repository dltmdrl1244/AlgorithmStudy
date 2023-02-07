n = int(input())
arr = []

for _ in range(n) :
    arr.append(list(map(int, input().split())))
    
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

def find_way(r, c) :
    if dp[r][c] != 0 :
        return dp[r][c]
    
    # 가로에서 찾기
    for i in range(c) :
        if arr[r][i] + i == c :
            dp[r][c] += find_way(r, i)
    
    #세로에서 찾기
    for i in range(r) :
        if arr[i][c] + i == r :
            dp[r][c] += find_way(i, c)
    
    return dp[r][c]
    
print(find_way(n-1, n-1))