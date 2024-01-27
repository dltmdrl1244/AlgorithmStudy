import sys
import math
input = sys.stdin.readline

def calculate(n, m):
    return (2 * n - 1) + math.ceil(abs(n * n - m) / n)

def bin_search(dist):
    left = 0
    right = dist

    while left <= right:
        mid = (left + right) // 2

        if mid * mid > dist:
            right = mid - 1
        elif mid * mid < dist:
            left = mid + 1
        else:
            return mid
    
    return right

for _ in range(int(input())):
    a, b = map(int, input().split())
    dist = b - a

    n = bin_search(dist)
    print(min(calculate(n, dist), calculate(n+1, dist)))