import sys
input = sys.stdin.readline

'''
첫번째 주사위가 어떤 면을 바닥으로 향하냐에 따라서 달라짐
a가 바닥으로 오면 f가 위로 오고 그러면 다음 주사위는 그 숫자의 인덱스가 바닥으로.
그럼 다시 그 반대편의 인덱스가 위로 올라온다.
그리고 바닥, 위를 제외한 숫자들 중에서는 회전이 가능하므로 가장 큰 수들끼리 모을 수 있다.

0-5, 1-3, 2-4
'''

n = int(input())
dices = []
oppo = [5, 3, 4, 1, 2, 0]
ans = 0

for _ in range(n):
    dices.append(list(map(int, input().split())))

for start_index in range(6):
    tmp = 0
    cur_bottom_number = dices[0][start_index]

    for dice in dices:
        cur_bottom_index = dice.index(cur_bottom_number)
        cur_top_index = oppo[cur_bottom_index]
        
        tmp_max = 0
        for i in range(6):
            if i == cur_bottom_index or i == cur_top_index:
                continue
            if dice[i] > tmp_max:
                tmp_max = dice[i]
        
        tmp += tmp_max            
        cur_bottom_number = dice[cur_top_index]

    ans = max(ans, tmp)

print(ans)