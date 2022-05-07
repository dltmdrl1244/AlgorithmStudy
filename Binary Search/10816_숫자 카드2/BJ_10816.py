import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))
answer = []

def binSearch(cards, start, end, n) :
    if start > end :
        return 0
    
    else :
        mid = (start + end) // 2
        
        if cards[mid] == n :
            return cards[start:end+1].count(n)
        
        elif cards[mid] < n :
            return binSearch(cards, mid + 1, end, n)
        else :
            return binSearch(cards, start, mid + 1, n)

cards.sort()

for s in search :
    answer.append(binSearch(cards, 0, n-1, s))

print(*answer)