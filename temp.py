import sys
n = int(sys.stdin.readline())
lista = list(map(int, sys.stdin.readline().split()))
listb = list(map(int, sys.stdin.readline().split()))
listc = []
sum = 0

lista.sort(key = lambda x : x)
listb.sort(key = lambda x : -x)

print(lista)
print(listb)

for i in range(n) :
    sum += lista[i] * listb[i]
    
print(sum)