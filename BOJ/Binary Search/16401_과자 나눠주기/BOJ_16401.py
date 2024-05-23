import sys
from bisect import bisect_left
input = sys.stdin.readline

'''
과자는 쪼갤수는 있지만 합쳐서 줄수는 없다.
과자를 정렬 싹 하고

1~n 까지의 막대 중에서 가운데 번째 m찾음
'이 길이 l로 다 나눠주기 가능?' 을 탐색 시작 -> 이 작업의 횟수는 log(N)

성공하면 -> 더 큰 길이로도 해봄. m+1 ~ n번째 중에서 다시 수행
실패하면 -> 더 작은 길이로 해봄. 1 ~ m-1번째 중에서 다시 수행
'''

def solve(left, right):
    global ans
    if left > right:
        return
    
    mid = (left + right) // 2
    if is_possible(mid):
        ans = max(ans, mid)
        solve(mid + 1, right)
    else:
        solve(left, mid - 1)


def is_possible(mid):
    cnt = 0
    start_index = bisect_left(arr, mid)
    for i in range(start_index, len(arr)):
        cnt += arr[i] // mid
        
    return True if cnt >= m else False

m, n = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

arr.sort()
solve(1, arr[-1])

print(ans)