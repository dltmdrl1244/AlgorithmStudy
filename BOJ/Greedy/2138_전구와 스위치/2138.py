import sys
input = sys.stdin.readline

def solve(first):
    arr = cur.copy()
    count = 0
    if first:
        press(arr, 0)
        count += 1
    
    for i in range(1, n):
        if arr[i-1] != target[i-1]:
            press(arr, i)
            count += 1
    
    return count if target[-1] == arr[-1] else sys.maxsize

def press(arr, switch):
    for i in range(-1, 2):
        if 0 <= switch + i < n:
            arr[switch + + i] = 0 if arr[switch + + i] == 1 else 1

n = int(input())
cur = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))
ans = min(sys.maxsize, solve(True), solve(False))

print(ans if ans != sys.maxsize else -1)