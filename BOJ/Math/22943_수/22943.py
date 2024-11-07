import sys
from itertools import permutations
input = sys.stdin.readline

def get_prime():
    for i in range(2, 100000):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * 2, 100000, i):
                is_prime[j] = False


def is_prime_sum(number):
    for prime in primes:
        if prime >= number // 2:
            return False
        if is_prime[number - prime] and prime != number - prime:
            return True
        
        
def is_prime_mul(number):
    for prime in primes:
        if prime >= number // 2:
            return False
        
        if number % prime == 0:
            if is_prime[number // prime]:
                return True
            
def divide(number):
    while number % m == 0:
        number //= m
    return number


def calc(number):
    return is_prime_sum(number) and is_prime_mul(divide(number))

is_prime = [False, False] + [True] * 99998
primes = []
n, m = map(int, input().split())
ans = 0
get_prime()


for combi in permutations(range(10), n):
    if combi[0] == 0:
        continue
    number = int(''.join(map(str, combi)))
    if (calc(number)):
        ans += 1

print(ans)