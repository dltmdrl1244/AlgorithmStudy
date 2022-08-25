# 문제
링크 : https://www.acmicpc.net/problem/1325
해결여부 : yes

# 코드
```
import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    q = deque()
    q.append(s)
    visited = [False] * (n+1)
    visited[s] = True
    cnt = 0
    while q:
        cur = q.popleft()
        for i in com[cur]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1

    return cnt

n, m = map(int, input().split())
com = [[] for _ in range(n+1)]


for _ in range(m):
    v1, v2 = map(int, input().split())
    com[v2].append(v1)
    
result = []
for i in range(n):
    result.append(bfs(i+1))

m = max(result)
answer = [i+1 for i in range(len(result)) if result[i] == m]
print(*answer)
```

# 문제 풀이
B컴퓨터가 A컴퓨터를 신뢰한다면, A컴퓨터를 해킹하면 B컴퓨터도 해킹 가능하다. 즉 간선이 단방향인 그래프를 그릴 수 있고 최대로 많이 연결된 노드를 찾는 문제로 해석 가능하다.

간선은 리스트에다가 `append` 하는 방식으로 저장하였고, 이후 BFS를 모든 노드에 대해 돌리고 그 결과를 `result` 리스트에 저장하였다. 이후 `result` 배열에서 최댓값을 가지는 인덱스를 출력한다.

# 부족했던 점

# 마무리
처음에 노드 개수가 최대 10,000개고 간선 개수가 최대 100,000개여서 시간초과가 났다. 더 시간을 줄일 수 있는 방법이 떠오르지 않아 pypy로 제출하였고 통과했다.