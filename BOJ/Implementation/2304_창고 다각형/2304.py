import sys
input = sys.stdin.readline

'''
첫 최댓값까지는 이전 스택보다 크지 않으면 넣지 않는다.
마지막 최댓값 이후로는 이 값보다 작은 것들을 다 빼고 넣는다.
'''

n = int(input())
columns = [list(map(int, input().split())) for _ in range(n)]
columns.sort(key = lambda x : (x[0]))

m = max(columns[i][1] for i in range(n))
maxes = [i for i in range(n) if columns[i][1] == m]
first_max = maxes[0]
last_max = maxes[-1]

ans = 0
prevX = 0
prevY = 0
stack = []
for i in range(first_max + 1):
    if stack and stack[-1][1] > columns[i][1]:
        continue
    stack.append(columns[i])
    ans += (columns[i][0] - prevX) * prevY
    prevX, prevY = columns[i]

ans += (columns[last_max][0] + 1 - columns[first_max][0]) * m

stack = []
for i in range(last_max, n):
    while stack and stack[-1][1] < columns[i][1]:
        stack.pop()
    
    stack.append(columns[i])

prevX = stack[0][0] + 1

for i in range(1, len(stack)):
    t = (stack[i][0] + 1 - prevX) * stack[i][1]
    ans += t

    prevX = stack[i][0] + 1

print(ans)