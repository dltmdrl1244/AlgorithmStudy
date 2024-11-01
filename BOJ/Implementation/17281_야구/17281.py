import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

def calc(orderIdx):
    global ans
    score = 0
    hitter_number = 0
    for inning in range(n):
        out_count = 0
        base1, base2, base3 = 0, 0, 0
        while out_count < 3:
            cur_hitter = orderIdx[hitter_number]
            
            if result[inning][cur_hitter] == 0:
                out_count += 1
                
            elif result[inning][cur_hitter] == 1: # 1루타
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1
                
            elif result[inning][cur_hitter] == 2: # 2루타
                score += base2 + base3
                base3 = base1
                base2 = 1
                base1 = 0
                
            elif result[inning][cur_hitter] == 3: # 3루타
                score += base1 + base2 + base3
                base3 = 1
                base2 = 0
                base1 = 0
                
            else: # homer
                score += 1 + base1 + base2 + base3 
                base1 = 0
                base2 = 0
                base3 = 0
                
            hitter_number += 1
            hitter_number %= 9
        
    
    ans = max(ans, score)


n = int(input())
ans = 0
result = [list(map(int, input().split())) for _ in range(n)]

for perm in permutations(range(1, 9), 8):
    order = list(perm[:3]) + [0] + list(perm[3:]) # 4번 타자는 0번 선수로 고정
    calc(order)

print(ans)