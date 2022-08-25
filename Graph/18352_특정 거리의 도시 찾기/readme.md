# 문제
링크 : https://www.acmicpc.net/problem/18352
해결여부 : yes

# 코드
```
import sys
from collections import deque
input = sys.stdin.readline

v, e, k, x = map(int, input().split())
edge = [[] for _ in range(v+1)]
for _ in range(e):
    v1, v2 = map(int, input().split())
    edge[v1].append(v2)
    
def bfs(start):
    q = deque()
    q.append([start, 0])
    visited = [False] * (v+1)
    result = []

    while q:
        curv, cnt = q.popleft()
        if cnt == k:
            result.append(curv)
            
        visited[curv] = True
        
        for e in edge[curv]:
            if not visited[e]:
                q.append([e, cnt+1])
                visited[e] = True
       
    result.sort()
    return result


result = bfs(x)
if result:
    for r in result:
        print(r)
else:
    print(-1)

```

# 문제 풀이
간선 정보를 `edge[출발노드]` 에다가 이어 붙이는 방식으로 하여 탐색 시간을 줄이고자 하였다. 그리고 `visited` 정보를 이용하여 앞서 방문한 적이 있는 노드는 건너뛰고, 방문한 적 없는 노드에 한해 큐에 추가하는 방식으로 한다. 추가할 때는 이전 노드의 `cnt`에 1을 추가하여 추가한다.

큐에 추가할 때 `visited`를 확인하고 넣어도 되고, 일단 다 넣고 나서 꺼낼 때 `curv`에서 `visited`를 확인하여 `continue` 해도 가능하다. (위의 코드의 경우 전자)

그리고 `cnt`가 `k`이면 `result` 배열에 추가하고 배열을 확인하고 결과를 출력한다.

# 마무리
노드와 간선의 숫자 범위가 십만, 백만 단위라서 모든 노드에 대해 2차원 리스트 등을 사용하면 메모리와 시간 초과가 발생할 것이다.