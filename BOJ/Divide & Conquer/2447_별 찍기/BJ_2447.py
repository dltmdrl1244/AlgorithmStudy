import sys
sys.setrecursionlimit(10**6)

def append_star(n) :
    if n == 1 :
        return ['*']
    
    L = []
    # 크기가 n/3 by n/3인 사각형을 재귀 호출하여 stars에 저장.
    # 이 stars의 각 라인을 여러번 곱하고 이어붙이는 식으로 정답 L을 만들어 낼 것
    stars = append_star(n//3)

    # 첫 번째, 세 번째 부분은 이 전 단계의 사각형 3개를 이어붙인 모양을 띤다.
    # stars는 n/3 줄, 즉 n/3개의 원소를 가지는 리스트 형태이다.
    for star in stars :
        L.append(star * 3)
    # 두 번째 부분은 중간에 n/3 by n/3 크기의 공백이 있어야 한다.
    # 그래서 하나와 하나 사이에 공백을 n/3개씩 만들어서 이어 붙인다.
    for star in stars :
        L.append(star + ' ' * (n//3) + star)
    for star in stars :
        L.append(star * 3)
        
    # 총 n/3 * 3 = n번 이어 붙여서 n x n 모양의 리스트 L이 생성되었음
    return L

n = int(sys.stdin.readline().strip())
# list 사이사이에 \n을 join 시킨다.
print("\n".join(append_star(n)))

# 분할하여 작은 사각형을 만들어 이어 붙이는 것까지는 생각을 했었는데
# 1번째 사각형, 2번째 사각형, 3번째 사각형 이런 식으로 이어 붙일 수 있는게 아니라 출력의 특성상
# 1번째 사각형의 첫줄, 2번째 사각형의 첫줄, 3번째 사각형의 첫줄, 다시 1번째 사각형의 두번째줄... 이런 식으로
# 이어 붙여야 한다는 것에 좋은 아이디어가 떠오르지 않아 결국 검색하여 정답을 보았음.
# 이전 단계의 사각형을 이어 붙일 때 곱하기 3을 해서 더 큰 리스트를 만들어서 리스트의 원소들을 한 줄씩 출력하는 깔끔한 풀이를 찾았고 이해하였다.
# 다음에는 나도 이런 멋진 생각을 할 수 있었으면...