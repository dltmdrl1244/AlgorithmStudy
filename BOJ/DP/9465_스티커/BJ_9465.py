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
    s = rotated(s) # s의 인덱스에 접근하기 용이하게 오른쪽으로 90도 회전
    s.insert(0, [0, 0])
    
    dp[1] = s[1]
    if n == 1 :
        print(max(dp[1]))
        continue
    # n이 1이면 바로 dp[1] 중 큰 값 출력
    
    dp[2][0] = dp[1][1] + s[2][0]
    dp[2][1] = dp[1][0] + s[2][1]
    if n == 2 :
        print(max(dp[n]))
        continue
    # n이 2이면 바로 대각선 앞의 값 + s[2]값
    
    for i in range(3, n+1) :
        dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + s[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + s[i][1]
    # n이 3 이상이면 점화식을 사용함. 대각선 바로 앞 칸과 그 앞 칸까지의 최댓값에 현재 칸의 값을 더한 값이 dp값
        
    print(max(dp[i]))
    