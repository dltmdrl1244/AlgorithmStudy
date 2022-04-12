import sys
n = int(sys.stdin.readline())
lista = list(map(int, sys.stdin.readline().split()))
listb = list(map(int, sys.stdin.readline().split()))
listc = []
sum = 0

lista.sort(key = lambda x : x)
listb.sort(key = lambda x : -x)


for i in range(n) :
    sum += lista[i] * listb[i]
    
print(sum)

# 두 리스트 원소끼리의 곱의 합이 최소가 되려면 어떤 큰 값에 곱해지는 수는 반대편 리스트에서 비교적 작은 수여야 한다.
# 즉 한 리스트는 오름차순 정렬하고, 다른 한 리스트는 내림차순 정렬하여 서로 곱하면 최소합이 나온다.
