from collections import deque

def hackerlandRadioTransmitters(x, k):
    x.sort()
    ans = 0
    q = deque([])
    coverage = 0
    prev = 0
    for i in range(len(x)):
        cur = x[i]
        if cur <= coverage:
            continue

        if not q or (q and q[0] + k >= cur):
            q.append(cur)
            prev = cur
        
        elif q and q[0] < cur:
            ans += 1
            coverage = prev + k
            q.clear()
            if cur > coverage:
                q.append(cur)
            prev = cur
    
    return (ans + 1 if q else ans)



n, k = map(int, input().split())
arr = list(map(int, input().split()))

hackerlandRadioTransmitters(arr, k)