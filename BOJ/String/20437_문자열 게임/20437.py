import sys
input = sys.stdin.readline

def get_ord(a):
    return ord(a) - ord('a')

def solve():
    arr = list(input().rstrip())
    k = int(input())
    ans1 = sys.maxsize
    ans2 = 0
    counter = [[] for _ in range(26)]
    
    for idx, l in enumerate(arr):
        alphabet = get_ord(l)
        counter[alphabet].append(idx)
        if len(counter[alphabet]) >= k:
            ans1 = min(ans1, idx - counter[alphabet][-k] + 1)
            ans2 = max(ans2, idx - counter[alphabet][-k] + 1)

    if ans1 == sys.maxsize:
        print(-1)
    else:
        print(ans1, ans2)


for _ in range(int(input())):
    solve()