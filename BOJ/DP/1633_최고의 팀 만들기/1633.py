import sys
from collections import defaultdict
input = sys.stdin.readline

lines = sys.stdin.readlines()
arr = []
dp = defaultdict(int)
n = 0

def dfs(r_b, r_w, idx):
    if idx >= n:
        return 0
    if r_b == 0 and r_w == 0:
        return 0

    if (r_b, r_w, idx) in dp:
        return dp[(r_b, r_w, idx)]
    
    res = dfs(r_b, r_w, idx + 1)
    if r_b > 0:
        res = max(res, dfs(r_b-1, r_w, idx+1) + arr[idx][0])
    if r_w > 0:
        res = max(res, dfs(r_b, r_w-1, idx+1) + arr[idx][1])
    
    dp[(r_b, r_w, idx)] = res
    return res
        

for line in lines:
    b, w = line.split()
    arr.append((int(b), int(w)))
    n += 1
    
print(dfs(15, 15, 0))