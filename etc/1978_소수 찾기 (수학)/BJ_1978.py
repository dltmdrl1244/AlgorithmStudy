import sys
input = sys.stdin.readline

# 2부터 루트N까지 나누어 떨어지는 수가 없으면 소수이다.
def isPrime(n) :
    if n == 1 :
        return False
    i = 2
    while i**2 <= n :
        if n % i == 0 :
            return False
        i += 1
    return True

_ = int(input())
p = list(map(int, input().split()))
answer = 0

for i in p :
    if isPrime(i) :
        answer += 1

print(answer)