import sys
input = sys.stdin.readline

def root(p):
    while p != ids[p]:
        if p == m:
            return -1
        p = ids[p]

    if p == m:
        return -1
    return p

n = int(input())
ids = [i for i in range(n)]
s = list(map(int, input().split()))
m = int(input())
parents = set()
nodes = set()

for i in range(n):
    ids[i] = s[i] if s[i] != -1 else i

for i in range(n):
    if root(i) != -1:
        # 루트 노드가 곧 리프 노드인 케이스 방지
        if i != root(i):
            parents.add(ids[i])
        nodes.add(i)

print(len(nodes) - len(parents))