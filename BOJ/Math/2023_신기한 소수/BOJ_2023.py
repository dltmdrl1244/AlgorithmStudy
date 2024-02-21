import sys
input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** (1/2) + 1)):
        if n % i == 0:
            return False
    return True
        
def dfs(num):
    if len(str(num)) == n:
        print(num)
        
    for i in range(10):
        if is_prime(num*10+i):
            dfs(num*10+i)

n = int(input())

for i in [2, 3, 5, 7]:
    dfs(i)