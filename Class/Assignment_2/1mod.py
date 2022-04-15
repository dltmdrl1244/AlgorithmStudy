import sys

n = int(sys.stdin.readline())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 중복 제거
coord_point = list(set(map(tuple, points)))

def dist(a, b) :
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 
    
def solve(start, end, arr) :
    # print("=== start solve(%d, %d)"%(start, end), arr, "start ===")
    if start == end :
        return [float('inf'), arr]
    
    elif end - start == 1 :
        if arr[start][1] > arr[end][1] :
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
        return [dist(arr[start], arr[end]), arr]
    
    mid = (start + end) // 2
    # print("mid : %d" %mid)
    # print(arr[:mid + 1], arr[mid + 1:])
    
    left_d, left_arr = solve(0, len(arr[:mid+1]) - 1, arr[:mid + 1])
    # print("left arr :", left_arr, "left_d :", left_d)
    right_d, right_arr = solve(0, len(arr[mid+1:]) - 1, arr[mid + 1:])
    # print("right arr :", right_arr, "right_d :", right_d)

    d = min(left_d, right_d)

    # d = min(solve(start, mid)[0], solve(mid+1, end)[0])
    # print("d :", d)
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
    # print("(end)new_arr :", new_arr)
    
    # print("mid :", arr[mid])
    
    candidate = []
    for i in range(start, end + 1) :
        if (new_arr[i][0] - arr[mid][0]) ** 2 < d :
            candidate.append(new_arr[i])
    
    # print("candidate :", candidate)
    
    can_len = len(candidate)
    for i in range(can_len - 1) :
        for j in range(i + 1, can_len) :
            if i - j > 12 :
                break
            if (candidate[i][1] - candidate[j][1]) ** 2 < d :
                d = min(d, dist(candidate[i], candidate[j]))
            else :
                break
    # print("(end)d :", d)
    # print("===end solve(%d, %d)"%(start, end), arr, " end===")

    return [d, new_arr]
        

if len(points) != len(coord_point) :
    print("0")
else :
    points = sorted(points, key = lambda x : x[0])
    print(solve(0, n-1, points)[0])