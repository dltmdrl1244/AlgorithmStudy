import sys

n = int(sys.stdin.readline())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 중복 제거
coord_point = list(set(map(tuple, points)))

def dist(a, b) :
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 
    
def solve(N, arr) :
    # 점 개수가 하나이면 거리 개념이 없으므로 무한대 리턴
    if N == 1 :
        return [float('inf'), arr]
    # 점 개수가 두 개이면 두 점을 y좌표 비교하여 정렬해서 리턴한다
    # 두 점을 정렬할 때 시간 복잡도는 O(1)
    elif N == 2 :
        if arr[0][1] > arr[1][1] :
            temp = arr[0]
            arr[0] = arr[1]
            arr[1] = temp
        return [dist(arr[0], arr[1]), arr]
    
    # 가운데 점을 기준으로 자른다. (홀수 일때는 앞부분이 1 더 크다. ex: 7일 때 0~3, 4~6)
    mid = N // 2
    
    # 양 쪽의 최소 거리를 구한다. 이 때 점의 개수는 
    left_d, left_arr = solve(len(arr[:mid+1]), arr[:mid + 1])
    right_d, right_arr = solve(len(arr[mid+1:]), arr[mid + 1:])
    d = min(left_d, right_d)
    # left_d, right_d 중 작은 값을 d에 저장. 이제 이 d을 가운데 경계 조사 케이스랑 비교한다.
    
    # left_arr과 right_arr은 길이가 N/2이고, y축좌표 기준으로 정렬되어 있다. 이를 병합한다.
    # 병합하는 과정에서의 시간 복잡도는 O(n)
    i, j = 0, 0
    lena = len(left_arr)
    lenb = len(right_arr)
    new_arr = []
    while i < lena and j < lenb :
        if left_arr[i][1] <= right_arr[j][1] :
            new_arr.append(left_arr[i])
            i += 1
        else :
            new_arr.append(right_arr[j])
            j += 1
    
    while i < lena :
        new_arr.append(left_arr[i])
        i += 1
    while j < lenb :
        new_arr.append(right_arr[j])
        j += 1
    
    # candidate 리스트는 경계선으로부터 x좌표가 d 이내인 점들의 리스트 (1차로 거르기)
    candidate = []
    for i in range(N) :
        if (new_arr[i][0] - arr[mid][0]) ** 2 < d :
            candidate.append(new_arr[i])
    
    
    can_len = len(candidate)
    for i in range(can_len - 1) :
        for j in range(i + 1, can_len) :
            # candidate 리스트가 이미 y축 기준으로 정렬이 되어 있으므로, 한 번 d보다 멀리 떨어진 점이 등장하면
            # 그 뒤로는 볼 필요가 없다. break
            # 이 때, j for문은 최악의 경우에도 12번까지만 돌게 된다.
            if (candidate[i][1] - candidate[j][1]) ** 2 < d :
                d = min(d, dist(candidate[i], candidate[j]))
            else :
                break
            
    # 1, 2, 3번 케이스를 모두 고려하였으므로 
    return [d, new_arr]
        
# 중복을 제거한 리스트와, 처음 리스트의 개수가 다르면 중복, 즉 같은 좌표가 있다는 소리니까 0
if len(points) != len(coord_point) :
    print("0")
else :
    points = sorted(points, key = lambda x : x[0])
    print(solve(n, points)[0])