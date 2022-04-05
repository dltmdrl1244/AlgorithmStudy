import sys
import time
from random import *

n = int(sys.argv[1])

array = []

for i in range(n):
    array.append(randrange(-25, 25))

begin = time.time()

# <--------------- 나만의 알고리즘
dynamic_array = [0 for _ in range(n)]
dynamic_array[0] = array[0]

for i in range(1, n) :
    dynamic_array[i] = max(dynamic_array[i - 1] + array[i], dynamic_array[i - 1])

max = max(dynamic_array)

# ------------------------------->

end = time.time()

print(f'Elapsed time: {end-begin:.7f} sec')