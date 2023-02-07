import sys
input = sys.stdin.readline

n = int(input())
dic = {}
cards = list(map(int, input().split()))
answer = []

# 카드들을 딕셔너리에 저장
for c in cards :
    if c in dic :
        dic[c] += 1
    else :
        dic[c] = 1

m = int(input())
search = list(map(int, input().split()))

# 딕셔너리에서 탐색
for s in search :
    if s in dic :
        answer.append(dic[s])
    else :
        answer.append(0)

print(*answer)

# 풀긴 했는데 딕셔너리 사용한 것이라서... 이진 탐색으로도 풀어보자.