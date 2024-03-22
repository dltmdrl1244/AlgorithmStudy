def solution(N, number):
    answer = 1
    dp = [set() for i in range(9)]

    if N == number:
        return answer
    
    for cnt in range(2, 9):
        dp[cnt].add(int(str(N) * cnt))
        for i in range(1, cnt):
            j = cnt - i
            for item1 in dp[i]:
                for item2 in dp[j]:
                    dp[cnt].update({item1+item2, item1-item2, item1*item2})
                    if item2 != 0:
                        dp[cnt].add(item1//item2)
                        
            if number in dp[cnt]:
                return cnt
    
    return -1