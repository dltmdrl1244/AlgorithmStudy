import sys
T = int(sys.stdin.readline())

def rotated(arr) :
    n = len(arr)
    m = len(arr[0])
    result = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(n) :
        for j in range(m) :
            result[j][n-i-1] = arr[i][j]
            
    return result
    
    
for _ in range(T) :
    n = int(sys.stdin.readline())
    dp = [[0, 0] for _ in range(100001)]
    s = []
    
    for _ in range(2) :
        s.append(list(map(int, sys.stdin.readline().split())))
    s = rotated(s)
    s.insert(0, [0, 0])
    
    dp[1] = s[1]
    if n == 1 :
        print(max(dp[1]))
        continue
    
    dp[2][0] = dp[1][1] + s[2][0]
    dp[2][1] = dp[1][0] + s[2][1]
    if n == 2 :
        print(max(dp[n]))
        continue
    
    
    for i in range(3, n+1) :
        dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + s[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + s[i][1]
    print(max(dp[i]))
    