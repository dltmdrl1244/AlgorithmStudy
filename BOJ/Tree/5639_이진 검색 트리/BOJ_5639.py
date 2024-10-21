import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def recur(arr):
    if len(arr) == 0:
        return
    tmp = arr[0]
    left, right = 1, len(arr) - 1
    
    # 이진 탐색으로 tmp보다 더 커지는 지점을 찾는다.
    while left <= right:
        midIdx = (left + right) // 2
        if arr[midIdx] > tmp:
            right = midIdx - 1
        else:
            left = midIdx + 1
    
    # 1~left-1 까지는 왼쪽 서브트리, left 부터는 오른쪽 서브트리이다.
    recur(arr[1:left])
    recur(arr[left:])
    print(tmp)

arr = []
while True:
    tmp = input()
    if tmp == '':
        break
    arr.append(int(tmp))

recur(arr)