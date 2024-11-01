import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
check = defaultdict(int)
check_heap = []
stack = []
ans = 0

for _ in range(n):
    pos, h = map(int, input().split())
    
    # 이 그림자보다 높은 건물들은 더이상 이 오른쪽으로 갈 수 없으므로 모두 pop
    while stack and stack[-1] > h:
        ended = stack.pop()
        check[ended] = 0
        ans += 1
    
    if h > 0: # 0일때는 패스
        if check[h] == 0: # 여러 개 들어가지 않도록, 힙에 없을 때만 넣기
            stack.append(h)
        check[h] = 1 # 이 높이의 그림자는 아직 유효하다고 표시

ans += len(stack)

print(ans)