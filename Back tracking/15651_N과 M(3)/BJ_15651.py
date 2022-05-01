import sys
n, m = map(int, sys.stdin.readline().split())

s = []

def f() :
    if len(s) == m :
        print(" ".join(map(str, s)))
        return
    
    for i in range(1, n+1) :
        s.append(i)
        f()
        s.pop()
            
f()

# 중복을 허용하고 사전순으로만 배열하면 된다.
# for 루프에서 1부터 n까지 진행하므로 별다른 조건문 없이 for 루프만 있어도 된다.