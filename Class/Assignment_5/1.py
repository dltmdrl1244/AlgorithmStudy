import math

f = open("input.txt", "r")
f2 = open("output.txt", "w")
n = int(f.readline())
INF = 999999

pos = [list(map(int, f.readline().split())) for _ in range(n)]
graph = [[0 for _ in range(n)] for _ in range(n)]
dp = [[INF] * (1 << n) for _ in range(n)]
path = []

def getDist(Ax, Ay, Bx, By) :
    return round(math.sqrt((Ax - Bx) ** 2 + (Ay - By) ** 2), 3)

def dfs(start, visited) :
    if visited == (1 << n) - 1 :
        dp[start][visited] = graph[start][0]
        return graph[start][0]
    
    if dp[start][visited] != INF :
        return dp[start][visited]
    
    for i in range(1, n) :
        if visited & (1 << i) :
            continue
        dp[start][visited] = min(dp[start][visited], dfs(i, visited | (1 << i)) + graph[start][i]) 
    
    return dp[start][visited]

def printPath(k, visited) :
    path.append(k)
    
    if visited == (1 << n) - 1 :
        return
    
    # print(k, bin(visited))
    nextvalue = [INF, 9]
    for i in range(n) :
        # print("i :", i, (graph[k][i] + dp[i][visited | (1 << i)]))
        if visited & (1 << i) :
            continue
        if (graph[k][i] + dp[i][visited | (1 << i)]) < nextvalue[0] :
            nextvalue[0] = graph[k][i] + dp[i][visited | (1 << i)]
            nextvalue[1] = i
    # print("===================")
    printPath(nextvalue[1], visited | (1 << nextvalue[1]))
        

for i in range(n) :
    for j in range(n) :
        graph[i][j] = getDist(pos[i][0], pos[i][1], pos[j][0], pos[j][1])

f2.write(str(round(dfs(0, 1), 2)) + "\n")

printPath(0, 1)
path.append(0)
f2.write(",".join(map(str, path)))
print("finish")
