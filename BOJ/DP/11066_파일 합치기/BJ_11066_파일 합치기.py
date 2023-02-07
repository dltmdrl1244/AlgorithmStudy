import sys
input = sys.stdin.readline

def solve() :
    k = int(input())
    arr = [0] + list(map(int, input().split())) # 각 파일의 비용을 담고 있는 리스트
    s = [0] * (k+1) # 각 비용을 이용한 부분합을 담고 있는 리스트
    
    s[1] = arr[1]
    for i in range(2, k+1) :
        s[i] = s[i-1] + arr[i]
    # 이렇게 넣어놓으면 i부터 j까지의 합을 s[j] - s[i-1]로 구할 수 있다.
    
    dp = [[0] * (k+1) for _ in range(k+1)] 
    # dp[i][j]는 i번째 파일부터 j번째 파일까지를 합치는 데 필요한 최소 비용을 담고 있다
    # 즉 우리가 구해야 하는 것은 dp[1][n]
    
    for n in range(2, k+1) : # 길이. 최대 k까지 돌아야 하므로 range는 2, k+1
        for i in range(1, k-n+2) : # 시작 위치. 길이가 n일때 1,2,...n 부터 시작해서 k-(n-1),...k-1,k까지 돈다. 
            #예를 들어 길이가 2면 k-1까지 돌아야한다.
            
            dp[i][i+n-1] = min(dp[i][j] + dp[j+1][i+n-1] for j in range(i, i+n-1)) + (s[i+n-1] - s[i-1])
            # j는 중간에 잘리는 위치. (i, i+n-1) 에서 j가 될 수 있는 것은 i부터 i+n-2까지.
            # 그리고 뒤에 i부터 i+n-1까지의 부분합을 더해준다. (s 리스트 이용)
            
    print(dp[1][k])
        

for _ in range(int(input())) :
    solve()
