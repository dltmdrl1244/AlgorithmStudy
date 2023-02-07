import sys
input = sys.stdin.readline
n = int(input())

stack = []
cnt = 0
row = [0] * n

def is_possible(x, y) :
    for i in range(x) :
        if row[i] == y or abs(row[i] - y) == abs(i - x) :
            return False
    return True

for i in range(n-1, -1, -1) :
    stack.append([0, i])

while len(stack) != 0 :
    popx, popy = stack.pop()
    if popx == n - 1 :
        cnt += 1
        continue
        
    row[popx] = popy
    
    for i in range(n-1, -1, -1) :
        if is_possible(popx+1, i) :
            stack.append([popx+1, i])

print(cnt)

# 재귀호출이 아니라 스택을 이용하여 풀었다.
# 첫 행의 모든 좌표를 우선 스택에 push (앞에서부터 보기 위해 거꾸로 넣었다.)
# 스택에서 pop된 좌표를 가지고 queen을 배치하고, 앞서 배치된 queen을 고려하여 promising한 곳의 좌표를 다시 stack에 push 한다.
# 스택에서 pop 될 때에 x좌표가 n, 즉 마지막 행에 있었다면 queen이 n개만큼 가득 찬거니까 성공한 case, 즉 cnt 1 늘려주고 바로 continue
# 이렇게 해서 모든 경우의 수를 확인하여 stack이 빌 때까지 반복하면 된다.
# 아이디어 출처 : https://idea-sketch.tistory.com/29