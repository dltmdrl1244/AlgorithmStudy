import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
robot = deque([False for _ in range(n)])
belt = deque(list(map(int, input().split())))
d = belt.count(0)
ans = 1

while d < k:
    # 벨트 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = False

    # 로봇 이동
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i+1] = True
            robot[i] = False
            belt[i+1] -= 1
            
            if belt[i+1] == 0:
                d += 1

        robot[-1] = False
    
    # 로봇 올리기
    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

        if belt[0] == 0:
            d += 1
    
    ans += 1

print(ans - 1)