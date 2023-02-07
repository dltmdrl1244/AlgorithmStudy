import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
stack = []
answer = []
 
 
# 앞에서부터 탑을 탐색하고 스택에 집어넣는다.
# 이 때, 뒤에서 스택에 들어있는 탑보다 더 큰, 즉 높은 탑이 등장했으면, 스택 안에 들어 있는 탑들은 절대 신호를 받을 일이 없다. 자신한테 닿기 전에 뒤에서 받아버리니까
# 즉 필요없는 탑이 되는 것이다. 그래서 스택의 가장 뒤의 탑이 자신보다 크게 되거나, 또는 모두 pop되어 스택이 빌 때까지 pop을 수행한다.
# while문을 벗어나고 나면, stack 안의 상황은 다음과 같다.
# 1) 스택이 비어있는 경우 : 모든 탑이 자신보다 작다는 뜻이므로 신호를 받을 탑이 없다. -> 0 append
# 2) 스택이 비어있지 않는 경우 : 자신보다 큰 탑이 자신의 앞에 있다는 뜻이므로 신호를 받을 탑이 있고, 스택의 가장 뒤의 탑은 자신보다 큰 탑들 중 가장 자신과 가까운 탑이다. -> 그 탑의 index append
for i in range(n):
    while stack and stack[-1][1] < tower[i] :
        stack.pop()
    
    if stack :
        answer.append(stack[-1][0] + 1)
    else :
        answer.append(0)
    
    stack.append([i, tower[i]])
    
print(*answer)