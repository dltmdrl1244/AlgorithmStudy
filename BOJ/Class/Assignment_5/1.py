import math

f = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f.readline())
INF = 999999

pos = [list(map(int, f.readline().split())) for _ in range(n)] # 점 좌표
graph = [[0 for _ in range(n)] for _ in range(n)] # graph[i][j] = graph[j][i] = 점 i와 점 j 사이의 거리
dp = [[INF] * (1 << n) for _ in range(n)]
# dp[i][j] : i = 내 위치, j : 아직 방문하지 않은, 방문해야 할 노드 정보
# 들어가는 값은 남은 점들을 최적 경로로 돌았을 때의 총 거리
path = []

def getDist(Ax, Ay, Bx, By) : # 유클리드 거리 반환
    return round(math.sqrt((Ax - Bx) ** 2 + (Ay - By) ** 2), 3)

def dfs(start, visited) :
    # start : 현재 내 위치
    # visited : 방문 여부 정보를 담고 있음. 해당 비트가 0이면 방문하지 않은 것, 1이면 방문한 것
    if visited == (1 << n) - 1 : # 모든 정점 방문
        dp[start][visited] = graph[start][0]
        return graph[start][0]
    
    if dp[start][visited] != INF :
        return dp[start][visited]
    
    for i in range(1, n) :
        if visited & (1 << i) : # 0번 점은 시작점이니까 패스하고 1부터 본다. 방문한 점이라면 pass
            continue
        # 그 다음 점까지의 거리 + 그 다음 점에 방문하고 나서 남은 점들을 최적 경로로 돌았을 때의 거리
        # 의 합이 가장 작은 점이 현재 visited 상태 최적 경로 상의 다음 점이 될 것이다.
        dp[start][visited] = min(dp[start][visited], dfs(i, visited | (1 << i)) + graph[start][i]) 
    
    return dp[start][visited]

def printPath(k, visited) :
    # visited 상태에서, 남은 점들을 최적으로 돌 때, 다음으로 방문하는 점을 찾는다.
    path.append(k)
    
    if visited == (1 << n) - 1 :
        return
    
    nextvalue = [INF, 0]
    for i in range(n) :
        if visited & (1 << i) :
            continue
        # dp[i][visited] 현재 visited에서의 최적이 들어있고, 우리가 찾는건 다음의 최적 점이다.
        # 현재의 visited에 하나씩 비트 붙여가면서 값을 구했을 때, 그 값들 중 최솟값이 다음 최적 점이다. 
        if (graph[k][i] + dp[i][visited | (1 << i)]) < nextvalue[0] :
            nextvalue[0] = graph[k][i] + dp[i][visited | (1 << i)]
            nextvalue[1] = i
    
    # for loop 종료 시, nextvalue[0]에는 남은 점들을 최적으로 돌았을 때의 최소 거리가
    # nextvalue[1]에는 다음 점이 들어 있다
    
    printPath(nextvalue[1], visited | (1 << nextvalue[1])) # 반복.
        

for i in range(n) :
    for j in range(n) :
        graph[i][j] = getDist(pos[i][0], pos[i][1], pos[j][0], pos[j][1])

f2.write(str(round(dfs(0, 1), 2)) + "\n")

printPath(0, 1)
path.append(0)
f2.write(",".join(map(str, path)))
print("finish")
