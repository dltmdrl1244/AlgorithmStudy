import sys
import math
input = sys.stdin.readline
T = int(input())

def getDist(dot1, dot2) :
    return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)

def whereIsIt(dot, circle) :
    rad = circle[2]
    if getDist(dot, circle) > rad :
        return 1
    else :
        return 0
    


for _ in range(T) :
    ans = 0
    startX, startY, endX, endY = map(int, input().split())
    start = [startX, startY]
    end = [endX, endY]
    C = int(input())
    circles = [list(map(int, input().split())) for _ in range(C)]
    
    for c in circles :
        if whereIsIt(start, c) != whereIsIt(end, c) :
            ans += 1
    print(ans)
    
# 어떤 원을 기준으로, 출발점 도착점 두 점이 같은 영역(원의 내부 or 외부)에 존재하면, 원이 어디에 있건 얼마나 크건 간에 어떻게든 우회할 수 있는 길이 생긴다.
# 그런데 두 점이 서로 다른 영역에 있으면, 즉 한 점은 원 내부에, 한 점은 원 외부에 존재하면 무조건 원을 통과할 수 밖에 없다.
# 즉, 한 점이 이 원의 내부에 있는지, 외부에 있는지 중심으로부터의 거리와 반지름을 비교하여 판별하는 whereIsIt 함수를 만들어서, 두 원의 위치를 비교했을 때 영역이 서로 다르면 카운트를 늘려준다.
# 이 작업을 모든 원에 대해 수행하면 정답이 나온다.