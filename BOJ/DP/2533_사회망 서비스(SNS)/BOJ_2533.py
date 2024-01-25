import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
'''
어떤 서브 트리의 루트 노드가 ea이면, 루트의 직계 자손은 ea여도 되고 ea가 아니여도 된다. 이 중 작은 것을 취한다.
어떤 서브 트리의 루트 노드가 ea가 아니면, 루트의 직계 자손은 무조건 ea여야 한다
재귀적으로 루트 노드부터 리프 노드까지 탐색한다.
'''
def dfs(start):
    global visited
    global dp
    visited[start] = True

    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(nxt)
            dp[start][0] += dp[nxt][1]
            dp[start][1] += min(dp[nxt][0], dp[nxt][1])


n = int(input())
graph = [[] for _ in range(n+1)]
dp = [[0, 1] for _ in range(n+1)]
# dp[i][0] = i번째 노드가 ea가 아닐 때, i를 루트로 하는 서브 트리의 최소 ea 수
# dp[i][1] = i번째 노드가 ea일 때, i를 루트로 하는 서브 트리의 최소 ea 수. 자기 자신이 ea이므로 기본적으로 1을 가지고 시작
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)
print(min(dp[1][0], dp[1][1]))