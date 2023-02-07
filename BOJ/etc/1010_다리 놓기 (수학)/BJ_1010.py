import sys
import operator as op
from functools import reduce
n = int(sys.stdin.readline())

def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

for _ in range(n) :
    n, m = map(int, sys.stdin.readline().split())
    print(nCr(m, n))
    
# n <= m 이고 다리를 n개 짓는다. 이 때 다리는 서로 엇갈리면 안 된다.
# 간단히 생각해보면 m개 중 n개를 고르기만 하면 그 중에서 위에서부터 차례대로 매칭해주면 되는 거라
# 사실상 mCn을 푸는 문제이다