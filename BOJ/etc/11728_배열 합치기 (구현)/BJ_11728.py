import sys
n, m = map(int, sys.stdin.readline().split())
lista = list(map(int, sys.stdin.readline().split()))
listb = list(map(int, sys.stdin.readline().split()))
listc = []
indexa = 0
indexb = 0

while indexa != len(lista) and indexb != len(listb) :
    if lista[indexa] > listb[indexb] :
        listc.append(listb[indexb])
        indexb += 1
    else :
        listc.append(lista[indexa])
        indexa += 1

while indexa != len(lista) :
    listc.append(lista[indexa])
    indexa += 1

while indexb != len(listb) :
    listc.append(listb[indexb])
    indexb += 1

for c in listc :
    print(c, end=" ")
    
# merge sort에서 merge 하는 부분의 코드
# 간단함