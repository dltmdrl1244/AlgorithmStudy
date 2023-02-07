import sys
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

for tg in target :
    left = 0
    right = n - 1
    flag = 0
    
    while left <= right :
        mid = (left + right) // 2
        
        if tg == cards[mid] :
            print(1, end=" ")
            flag = 1
            break
        elif tg > cards[mid] :
            left = mid + 1
        else :
            right = mid - 1
            
    if not flag :
        print(0, end=" ")