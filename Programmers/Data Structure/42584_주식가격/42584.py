def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    stack = []
    
    for idx, price in enumerate(prices):
        while stack and stack[-1][0] > price:
            _, popped_index = stack.pop()
            answer[popped_index] = idx - popped_index
        stack.append((price, idx))
    
    # 스택에 남아 있는 (가격이 떨어지지 않은) 시점을 처리
    while stack:
        _, popped_index = stack.pop()
        answer[popped_index] = n - popped_index - 1
    
    return answer