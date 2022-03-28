import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
arr = [[-1 for _ in range(1001)] for _ in range(1001)]
dp = [[-1 for _ in range(1001)] for _ in range(1001)]

for i in range(n) :
    arr[i+1][1:len(arr[i+1])] = list(map(int,sys.stdin.readline().split()))

dp[1][1] = arr[1][1]    

def find_candy(n, m) :
    
    if dp[n][m] != -1 :
        return dp[n][m]
    
    if n == 1 : 
        if m != 1 : # n이 1이고 m이 1이 아닌, 즉 첫 번째 칸을 제외하고 첫 번째 행에 있을 때
            dp[n][m] = find_candy(n, m-1)
    else : 
        if m == 1 : # n이 1이 아니고 m이 1인, 즉 첫 번째 칸을 제외하고 첫 번째 열에 있을 때
            dp[n][m] = find_candy(n-1, m)
        else : # 나머지 케이스
            dp[n][m] =  max(find_candy(n-1, m), find_candy(n, m-1))
            
    dp[n][m] += arr[n][m]
    
    return dp[n][m]
    
print(find_candy(n,m))