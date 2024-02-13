import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(a, b, c):
    global ans
    if not (a >= 0 and b >= 0 and c >= 0) or (a, b, c) in visited:
        return
    
    visited.add((a, b, c))
    
    if a == 0 and c not in ans:
        ans.add(c)
    
    # a에 있는 물을 b 또는 c로 붓기
    if a > 0:
        dfs(a - min(a, cb - b), b + min(a, cb - b), c)
        dfs(a - min(a, cc - c), b, c + min(a, cc - c))
    
    # b에 있는 물을 a 또는 c로 붓기
    if b > 0:
        dfs(a + min(b, ca - a), b - min(b, ca - a), c)
        dfs(a, b - min(b, cc - c), c + min(b, cc - c))
    
    # c에 있는 물을 a 또는 b로 붓기
    if c > 0:
        dfs(a + min(c, ca - a), b, c - min(c, ca - a))
        dfs(a, b + min(c, cb - b), c - min(c, cb - b))
    

ca, cb, cc = map(int, input().split())
ans = set()
visited = set()

dfs(0, 0, cc)

ans = list(ans)
ans.sort()
print(*ans)