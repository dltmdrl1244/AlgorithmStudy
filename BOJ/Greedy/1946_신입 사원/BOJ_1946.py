import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    candi = [list(map(int, input().split())) for _ in range(n)]
    candi.sort(key= lambda x: x[0])
    
    cnt = 1
    min_rank = candi[0][1]
    for i in range(1, n):
        if candi[i][1] < min_rank:
            min_rank = candi[i][1]
            cnt += 1
    print(cnt)