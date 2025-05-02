import sys
input = sys.stdin.readline

def fact(n):
    cnt = 1
    i = 1
    while i <= n:
        cnt *= i
        i += 1
    return cnt

def get_rank(num, used):
    rank = 0
    for i in range(1, num):
        if i not in used:
            rank += 1
    
    return rank + 1

def get_rank_number(rank, used):
    passed = 0
    for i in range(1, n + 1):
        if i in used:
            continue
        
        passed += 1
        if passed == rank:
            return i

def get_perm_number(perm):
    '''
    i번째 자리가 커버할 수 있는 순열 개수는 (n-i)!개
    즉 (i자리 숫자의 현재 랭크 - 1) x (n-i)! 개만큼을 더함
    
    2 4 3 1
    i 1 : 1xxx 지나감. 랭크2-1 x 6 = 6 더함
    i 2 : 21xx 23xx 지나감. 랭크3-1 x 2 = 4 더함
    i 3 : 241x 지나감 랭크2-1 x 1 = 1 더함
    내앞에 11개 있고 나는 12번째
    '''
    cnt = 0
    used = set()
    for i in range(1, n+1):
        rank = get_rank(perm[i-1], used)
        cnt += (rank - 1) * fact(n - i)
        used.add(perm[i - 1])
    
    return cnt + 1

def get_perm(m):
    '''
    i번째 자리에 오는 값은 m / (n-i)! 몫 만큼을 지나고 다음 수
    예를 들어 4자리일때 15가 주어지면 14를 가지고 14 / 3! = 2
    즉 그자리 숫자는 rank가 3인 수. 즉 3
    1xxx, 2xxx로 12개를 보내고 3xxx 임을 알 수 있다. 그리고 12를 차감.
    남은 2에 대해서도 2!로 나눈 몫 1
    rank가 2인 수가 온다. 31xx을 지나고 32xx임을 알 수 있다. 그리고 2를 차감. 0
    
    0이 되면 그때부터 가장빠른 순열을 만듬. 3214
    
    14로 시작하고 
    '''
    idx = 1
    used = set()
    result = []
    while m != 0:
        rank = m // fact(n-idx)
        target_number = get_rank_number(rank + 1, used)
        result.append(target_number)
        
        m -= rank * fact(n-idx)
        used.add(target_number)
        idx += 1
    
    while len(result) != n:
        target_number = get_rank_number(1, used)
        result.append(target_number)
        used.add(target_number)
        
    
    return result


n = int(input())
tmp = list(map(int, input().split()))


if tmp[0] == 1:
    print(*get_perm(tmp[1] - 1))

else:
    print(get_perm_number(tmp[1:]))