import sys
import math
import numpy as np

f = open("input.txt", "r")
s = list(map(int, f.readline().split()))
balloon = []
slope = []
slopes = []
maxb = []
answer = 0

def tan_point(Px, Py, Cx, Cy, r):
    b = math.sqrt((Px - Cx)**2 + (Py - Cy)**2)
    theta = math.acos(r / b)
    d = math.atan2(Py - Cy, Px - Cx)
    d1 = d + theta
    d2 = d - theta

    T1x = Cx + r * math.cos(d1)
    T1y = Cy + r * math.sin(d1)
    T2x = Cx + r * math.cos(d2)
    T2y = Cy + r * math.sin(d2)

    return ((T1x, T1y), (T2x, T2y))

def adjust(x) :
    return (x + 360) % 360

def find_angles(balloon):
    x, y, r = balloon
    tp1, tp2 = tan_point(0, 0, x, y, r)
    start_angle = round(adjust(math.atan2(tp1[1], tp1[0])/math.pi*180), 3)
    end_angle = round(adjust(math.atan2(tp2[1], tp2[0])/math.pi*180), 3)
    if (start_angle > end_angle):
        end_angle += 360

    return (start_angle, end_angle)


while True :
    b = list(map(float, f.readline().split()))
    if not b :
        break
    balloon.append([b[0] - s[0], b[1] - s[1], b[2]])
    
for b in balloon :
    slope.append(find_angles(b))

slope.sort(key = lambda x : x[1])

cross = [0 for _ in range(len(balloon))]
    
def handlerest(balloons, slopes, idx) :
    # print("idx :", idx)
    b = len(balloons)
    removed = [0] * b
    selected = slopes[idx]
    # print("selected :", selected)
    # print("cross :", cross)
    for i in range(b) :
        if cross[i] :
            if (0 <= selected and selected <= (slopes[i*2+1] % 360)) or (slopes[i*2] <= (selected % 360)) :
                removed[i] = 1
        else :
            if slopes[i*2] % 360 <= selected <= slopes[i*2+1] % 360 :
                removed[i] = 1
    
    cnt = 1
    last = 0
    for i in range(b) :
        if removed[i] == 0 :
            if last >= slopes[i * 2] :
                removed[i] = 1
            else :
                removed[i] = 1
                last = slopes[i * 2 + 1]
                cnt += 1
    return cnt


for i in range(len(slope)) :
    slopes.append(slope[i][0] % 360)
    slopes.append(slope[i][1] % 360)
    
    if (slope[i][0] - 360) * (slope[i][1] - 360) < 0 :
        cross[i] = 1

# for i in range(len(slope * 2)) :
#     print("%d : "%i, slopes[i])
    
maxans = 999
for i in range(len(balloon)) :
    res = handlerest(balloon, slopes, i * 2)
    maxans = min(maxans, res)

print("answer :", maxans)
