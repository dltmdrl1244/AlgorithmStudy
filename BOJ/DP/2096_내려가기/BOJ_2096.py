import sys
input = sys.stdin.readline

n = int(input())
min_ans = max_ans = list(map(int, input().split()))

for _ in range(1, n):
    tmp_list = list(map(int, input().split()))
    min_tmp, max_tmp = [sys.maxsize] * 3, [0] * 3
    for j in range(3):
        for k in (-1, 0, 1):
            prevIdx = j + k
            if 0 <= prevIdx < 3:
                min_tmp[j] = min(min_tmp[j], min_ans[prevIdx] + tmp_list[j])
                max_tmp[j] = max(max_tmp[j], max_ans[prevIdx] + tmp_list[j])

    min_ans = min_tmp
    max_ans = max_tmp

print(max(max_ans), min(min_ans))