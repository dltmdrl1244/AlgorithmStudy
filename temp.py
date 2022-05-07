import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
res = [0] * n

for i in range(len(tower)) :
    for j in range(i, -1, -1) :
        if tower[i] < tower[j] :
            res[i] = j + 1
            break

print(" ".join(map(str, res)))