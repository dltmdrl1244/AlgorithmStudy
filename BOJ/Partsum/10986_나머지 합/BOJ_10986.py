import sys
input = sys.stdin.readline
'''
i~j 까지의 합 = s[j] - s[i-1]
이것이 m의 배수이려면 (s[j] % m) == (s[i-1] % m)s
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = [0] * n
t = 0
rest = {0: 1}
answer = 0

for i in range(n):
    t += arr[i]
    s[i] = t

    if (t % m) in rest:
        answer += rest[t % m]
        rest[t % m] += 1
    else:
        rest[t % m] = 1
    
print(answer)