import sys
import math
input = sys.stdin.readline


def battle(room_idx):
    global delta, ans
    _, e_atk, e_health = rooms[room_idx]

    attack_count = math.ceil(e_health / atk)
    delta -= (attack_count - 1) * e_atk
    ans = min(ans, delta)
    

n, atk = map(int, input().split())
rooms = []
delta = 0
ans = sys.maxsize

for _ in range(n):
    rooms.append(list(map(int, input().split())))

for i in range(n):
    idx, a, h = rooms[i]
    if idx == 1: # 몬스터
        battle(i)

    else:
        atk += a
        delta = min(0, delta + h)

print(-ans + 1)