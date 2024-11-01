# 문제
링크 : [1613 역사](https://www.acmicpc.net/problem/1613)

해결여부 : yes

# 문제 풀이
> DFS 응용 또는 플로이드 와샬
## DFS
- 사건의 순서가 A->B->C 라면 A->C라는 사실도 바로 알 수 있어야 한다.
- 그래서 DFS를 수행하면서 이전에 거쳐온 노드들을 모두 저장하고 있다가 방문하지 않은 새로운 노드를 발견하면 이전 노드들의 정보까지도 한꺼번에 바꿔준다. (`hist` 이용)
- 그리고 항상 그래프의 끝에서부터 시작하리라는 법은 없다. 예를 들어 1 -> 2 -> 3 -> 4 일때 2를 먼저 방문한 후에 1을 방문하면 2가 이미 방문되었기 때문에 3, 4에 대한 정보를 갱신하지 못한 채 끝나게 된다. 따라서 이미 방문된 노드를 만나면 그 노드의 결과를 보고 true인 노드들(갈수있는 노드들)을 붙여넣기 한다.

## 플로이드 와샬
- 플로이드 와샬은 어떤 두 정점 s, e 간의 최단거리 또는 연결 여부를 판단할 때, 그래프 상에 있는 임의의 중간점 m을 거쳐 최단거리가 짧아지는지 or 연결되는지 갱신하는 알고리즘이다.
- 이 문제에도 적용 가능하며, A사건이 B사건보다 먼저 일어났고, B사건이 C사건보다 먼저 일어났다면 (A->B, B->C) A사건도 C사건보다 먼저 일어났음이 자명하기 때문이다. (A->C)
- 최단거리가 아니라 연결 여부만을 따지기 때문에 단방향 그래프를 입력 받을 때, `connected` 라는 불리언
배열을 사용할 수 있고 중간점 m을 거쳐 `connected[s][m]`과 `connected[m][e]`가 모두 true라면 `connected[s][e]`도 true로 만들어 준다.

```python
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
connected = [[False for _ in range(n+1)] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    connected[a][b] = True

for i in range(1, n+1):
    connected[i][i] = True

for m in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if connected[s][m] and connected[m][e]:
                connected[s][e] = True

for _ in range(int(input())):
    a, b = map(int, input().split())
    if connected[a][b] == True and connected[b][a] == False:
        print(-1)
    elif connected[a][b] == False and connected[b][a] == True:
        print(1)
    elif connected[a][b] == False and connected[b][a] == False:
        print(0)
```

# 마무리
근데 플로이드 와샬 알고리즘을 사용하면 python3로는 시간초과가 뜨고 pypy로는 통과된다.
3중 for문을 사용하는데 n <= 400이기 때문에 6400만 정도라서 가능할 줄 알았는데 흠...