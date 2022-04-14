import functools
import sys
n = int(sys.stdin.readline())
numbers = []

for i in str(n) :
    numbers.append(int(i))

# 30의 배수, 즉 3의 배수는 각 자리 수의 합이 3의 배수인 특징이 있다
if sum(numbers) % 3 != 0 :
    print(-1)
    exit()

# 수를 이리저리 조합해서 가장 크게 나오려면 내림차순으로 정렬.
numbers.sort(reverse=True)

a = functools.reduce(lambda x, y: 10 * x + y, numbers, 0)

# 30의 배수여야 하므로, 내림차순 정렬하여 하나로 뭉쳤을 때 마지막 자리가 0이어야 함
if a % 10 != 0 :
    print(-1)
    exit()
else :
    print(a)