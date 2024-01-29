from itertools import product
import sys
input = sys.stdin.readline

channel = int(input())
m = int(input())
d = set((map(int, input().split())))

s = len(list(str(channel)))
# 100번에서 +, - 버튼만 눌러서 원하는 채널 가는 횟수를 기본값으로 잡음
ans = abs(100 - channel)

# 고장난 버튼을 제외하고 나머지 버튼들로 만들 수 있는 숫자들을 모두 만들어 본다
for i in range(1, min(7, s + 2)):
    for p in product([i for i in range(10) if i not in d], repeat = i):
        num = int(''.join(map(str, p)))
        ans = min(ans, i + abs(channel - num))

print(ans)