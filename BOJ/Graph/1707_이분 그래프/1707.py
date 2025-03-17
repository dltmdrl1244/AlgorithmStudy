import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, visited, graph, v):
    q = deque()
    flags = [None] * (v+1)
    q.append(start)
    visited[start] = True
    flags[1] = True
    
    while q:
        cur = q.popleft()
        
        for nxt in graph[cur]:
            if flags[nxt] != None and flags[nxt] == flags[cur]:
                return False
            
            if flags[nxt] is None:
                q.append(nxt)
                flags[nxt] = not flags[cur]
                visited[nxt] = True
            
    return True

def solve():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    for i in range(1, v+1):
        if not visited[i]:
            if (not bfs(i, visited, graph, v)):
                print("NO")
                return
    
    print("YES")


for _ in range(int(input())):
    solve()