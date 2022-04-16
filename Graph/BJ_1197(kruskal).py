import sys
v, e = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]
parent = [i for i in range(v+1)]
result = 0

# kruskal 알고리즘을 이용하여 풀었다.

# 어떤 노드 X의 부모 노드를 찾는다.
# x의 find(x)가 자기 자신이 아니면, 그 x는 부모가 아니고 다른 어떤 노드의 자식이다
# 재귀적으로 건너 건너 가서, 마지막에 find(x)가 x가 될 때가 있는데 그것이 처음 x의 부모이다.
# find 값이 같은 두 점은 서로 이어져 있다고 볼 수 있다.
def find(parent, x) :
    if parent[x] == x :
        return x
    else :
        return find(parent, parent[x])

# 두 노드 a, b를 서로 연결한다. (자식-부모 관계로 만든다)
# 둘 중 누가 자식이 되고 부모가 되는지는 어찌 되든 상관없지만, 여기서는 값이 큰 애가 부모가 된다.
def union(parent, a, b) :
    a = find(parent, a)
    b = find(parent, b)
    if a > b :
        parent[b] = a
    else :
        parent[a] = b

# 간선들의 비용 순으로 오름차순 정렬한다.
edges.sort(key = lambda x : x[2])

# 간선들을 하나씩 살펴보면서 find 값, 즉 부모가 다른 노드들을 잇는 간선이 등장하면
# 둘을 이어 주고, 그 간선의 비용을 총 비용에 더한다.
for edge in edges :
    v1, v2, cost = edge
    if find(parent, v1) != find(parent, v2) :
        union(parent, v1, v2)
        result += cost
        
print(result)