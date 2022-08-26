from collections import deque
check = [False] * 100002
dist = [-1] * 100002

n,k = map(int, input().split())

def bfs(n, k):
    q = deque()
    q.append(n) 

    cnt = [-1 for _ in range(100001)]
    cnt[n] = 0
    
    while q:
        s = q.popleft()
        if s == k:
            return cnt[s]
        if 0 <= s-1 < 100001 and cnt[s-1] == -1:
            cnt[s-1] = cnt[s] + 1
            q.append(s-1)
        if 0 < s*2 < 100001 and cnt[s*2] == -1:
            cnt[s*2] = cnt[s]
            q.appendleft(s*2)
        if 0 <= s+1 < 100001 and cnt[s+1] == -1:
            cnt[s+1] = cnt[s] + 1
            q.append(s+1)

print(bfs(n, k))