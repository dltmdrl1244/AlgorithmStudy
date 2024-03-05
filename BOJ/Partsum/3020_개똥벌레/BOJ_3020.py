import sys
from collections import defaultdict
input = sys.stdin.readline

n, h = map(int, input().split())
jong = defaultdict(int)
seok = defaultdict(int)

for i in range(n):
    a = int(input())
    # 석순
    if i % 2 == 0:
        seok[a] += 1
    # 종유석
    else:
        jong[a] += 1
# 길이가 더 긴 것들을 짧은 쪽에 더해주면서 부숴야 하는 개수를 구한다
for i in range(h, 0, -1):
    seok[i-1] += seok[i]
    jong[i-1] += jong[i]

ans_val = sys.maxsize
ans_cnt = 0
for i in range(1, h+1):
    # i 구간에서는 길이가 i인 석순과 h+1-i인 종유석을 부순다
    val = seok[i] + jong[h+1-i]
    if ans_val > val:
        ans_val = val
        ans_cnt = 1
    elif ans_val == val:
        ans_cnt += 1

print(ans_val, ans_cnt)