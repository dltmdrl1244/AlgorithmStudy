# 최대 부분합 구하기 문제
# N개의 정수가 주어질 때 가장 큰 합을 가지는 구간을 구하여 그 합을 출력
import sys
import time
from random import *

n = int(sys.argv[1])

array = []

# 난수 생성하여 array 생성
for i in range(n):
    array.append(randrange(-25, 25))

# 시간 측정 시작
begin = time.time()

# <--------------- 나만의 알고리즘
# 동적 계획법으로 부분합을 저장할 리스트 생성
dynamic_array = [0 for _ in range(n)]
# dp[0]까지의 최대 누적합은 당연히 array[0]이다.
dynamic_array[0] = array[0]

# 일반화. i번째까지의 최대 누적합은 i-1까지의 최대 누적합에 i번째 값을 더하느냐, 더하지 않느냐로 결정된다.
# array[i]의 값이 0보다 크다면 당연히 dp[i-1]에 array[i]를 더한 값이 더 커지므로 더하게 될 것이고,
# array[i]의 값이 0보다 작다면 더했을 때 오히려 부분합이 더 작아지게 된다.
for i in range(1, n) :
    dynamic_array[i] = max(dynamic_array[i - 1] + array[i], dynamic_array[i - 1])

max = max(dynamic_array)

# ------------------------------->
# 시간 측정 종료
end = time.time()

print(f'Elapsed time: {end-begin:.7f} sec')