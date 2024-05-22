import sys
input = sys.stdin.readline


def is_available(lesson):
    for l in range(lesson[1], lesson[2] + 1):
        if s[lesson[0]][l]:
            return False
    return True

def apply(lesson):
    for l in range(lesson[1], lesson[2] + 1):
        s[lesson[0]][l] = True

def unapply(lesson):
    for l in range(lesson[1], lesson[2] + 1):
        s[lesson[0]][l] = False

def recur(idx, s, point, hist):
    global ans
    if point == k:
        ans += 1
        return
    
    if point > k or idx == n:
        return
    
    lesson = lessons[idx]
    if lesson[0] != 5 and is_available(lesson):
        apply(lesson) 
        recur(idx + 1, s, point + lesson[2] - lesson[1] + 1, hist + [idx+1])
        unapply(lesson)
        
    recur(idx + 1, s, point, hist)


n, k = map(int, input().split())
ans = 0
lessons = [list(map(int, input().split())) for _ in range(n)]

s = [[False for _ in range(11)] for _ in range(6)]

recur(0, s, 0, [])
print(ans)