import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

array = []
for i in range(0,n-1):
    array.append(sensors[i+1] - sensors[i])

array.sort()

print(sum(array[:n-k]))