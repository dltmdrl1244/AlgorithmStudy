import sys
input = sys.stdin.readline

n = int(input())
ans = 0
# A B C D E F
dice = list(map(int, input().split()))

if n == 1:
    print(sum(dice) - max(dice))
    sys.exit()

single = min(dice)
double = min([
    dice[0]+dice[1], dice[1]+dice[5], dice[0]+dice[4], dice[4]+dice[5],
    dice[3]+dice[0], dice[3]+dice[1], dice[3]+dice[4], dice[3]+dice[5],
    dice[2]+dice[0], dice[2]+dice[1], dice[2]+dice[4], dice[2]+dice[5]
])
triple = min([
    dice[3]+dice[0]+dice[1], dice[3]+dice[1]+dice[5], dice[3]+dice[0]+dice[4], dice[3]+dice[4]+dice[5], 
    dice[2]+dice[0]+dice[1], dice[2]+dice[1]+dice[5], dice[2]+dice[0]+dice[4], dice[2]+dice[4]+dice[5]
])

ans += (4 * (n-1) * (n-2) + (n-2) * (n-2)) * single
ans += (8 * (n) - 12) * double
ans += 4 * triple
print(ans)