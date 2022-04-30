import sys
n, m = map(int, sys.stdin.readline().split())

s = []

def f() :
    if len(s) == m :
        print(" ".join(map(str, s)))
        return
    
    for i in range(1, n+1) :
        if i not in s and (len(s) == 0 or i > s[-1]) :
            s.append(i)
            f()
            s.pop()
            
f()

# 백트래킹하는 알고리즘은 앞서 푼 N과 M(1) 문제(15649)와 동일하지만 오름차순이라는 제약사항이 추가된다.
# 즉 앞서 나온 숫자보다 작은 수가 나올 수 없으므로 이를 필터링하는 조건을 걸어준다.
# 새로 넣을 i가 s의 마지막 숫자보다 큰지 확인하고, s가 비어있을 때는 비교가 되지 않으므로 len(s) == 0 와 함께 or로 묶어준다.