import sys

n = int(sys.stdin.readline())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 중복 제거
coord_point = list(set(map(tuple, points)))

def dist(a, b) :
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 
    
def solve(start, end) :
    # 두 점의 최소 거리를 구할 때 고려할 케이스는 3가지이다.
    # 1) 중간 좌표로 구분선을 그었을 때 두 점이 모두 구분선 기준 왼쪽에 있는 경우
    # 2) 두 점이 모두 구분선 기준 오른쪽에 있는 경우
    # 3) 두 점이 양 쪽 구역에 하나씩 있는 경우
    
    # start와 end가 같은, 즉 점 개수가 하나인 경우에는 거리 개념이 없으므로 무한대 리턴
    if start == end :
        return float('inf')
    # start와 end가 1 차이, 즉 점 개수가 두 개인 경우에는 단순히 두 점의 거리 리턴
    elif end - start == 1 :
        return dist(points[start], points[end])
    
    # 그 밖의 경우, Divide & Conquer를 실행하여 1), 2)번 케이스의 최솟값을 구하여 answer에 저장
    mid = (start + end) // 2
    answer = min(solve(start, mid), solve(mid, end))
    
    # 3)번 케이스를 고려하기 위하여, 우선 구분선을 기준으로 x좌표가 answer 이하로 떨어진 점들만 candidate에 저장
    candidate = []
    for i in range(start, end + 1) :
        if (points[i][0] - points[mid][0]) ** 2 < answer :
            candidate.append(points[i])
    
    # 다음은 y좌표를 기준으로 다시 answer 이하로 떨어진 점들을 찾아야 하므로, candidate를 y좌표 기준으로 재정렬
    candidate.sort(key = lambda x : x[1])
    
    can_len = len(candidate)
    # 첫 번째 점, 즉 candidate 범위 안에서 가장 y좌표가 작은 점부터 시작하여 위로 올라가면서 y좌표를 비교
    # y좌표가 answer 이내라면, 최솟값이 될 가능성이 있으므로 거리를 직접 구해본다.
    # 만약 차이가 answer을 초과하는 점이 등장하면, y좌표로 정렬해 두었기 때문에 그 뒤로는 항상 answer 초과임. 즉 break
    # 중첩 for문으로 len(candidate)^2번 만큼 실행될 것 같으나 한 점을 기준으로 answer/2의 격자를 구성하면 위로 3칸 떨어진 부분을 벗어나면
    # 항상 answer보다 멀리 떨어져 있게 되므로, 더 이상 수행되지 않고 break를 만나게 된다
    for i in range(can_len) :
        for j in range(i+1, can_len) :
            if j - i > 12 :
                break
            if (candidate[i][1] - candidate[j][1]) ** 2 < answer :
                answer = min(answer, dist(candidate[i], candidate[j]))
            else :
                break
    # 1, 2, 3번 케이스를 모두 고려하였으므로 
    return answer 
    
# 원 리스트와 중복을 제거한 리스트의 길이가 다르면 중복된 점이 있는 것
# 따라서 최단 거리는 구할 것도 없이 0
if len(points) != len(coord_point) :
    print("0")
else :
    # line sweeping을 위해 x좌표 기준으로 정렬
    points = sorted(points, key = lambda x : x[0])
    print(solve(0, n-1))