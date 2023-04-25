import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
ids = [i for i in range(n+1)]
size = [1 for i in range(n+1)]

def find_cycle():
    def recur(start):
        visited[start] = True
        cycle_set.add(start)

        for nxt in graph[start]:
            if not visited[nxt]:
                recur(nxt)
            elif visited[nxt] and nxt in cycle_set:
                return True

        cycle_set.discard(start)
        return False


    visited = [False] * (n+1)
    cycle_set = set()

    for i in range(n):
        if not visited[i]:
            if recur(i):
                return True
    return False

def dfs(start):
    visited[start] = True
    
    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(nxt)
    
    topo.append(start)

for _ in range(k):
    t = list(map(int, input().split()))
    for i in range(1, len(t)-1):
        graph[t[i]].append(t[i+1])

if find_cycle():
    print(0)
    exit()
    
topo = []
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

topo.reverse()
print(*topo, sep="\n")