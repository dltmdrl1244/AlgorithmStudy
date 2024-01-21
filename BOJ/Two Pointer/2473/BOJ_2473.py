import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
minVal = sys.maxsize
ans = []

# 산도 순으로 정렬
arr.sort()

for i in range(n-2):
    # 하나를 고정해 두고 
    fix = arr[i]
    left = i + 1
    right = n - 1
    # 나머지 두 용액을 투 포인터로 조절해 간다
    while left < right:
        tmp = fix + arr[left] + arr[right]

        if minVal > abs(tmp):
            minVal = abs(tmp)
            ans = [fix, arr[left], arr[right]]
        # 만약 음수라면, 작은 값(left)를 더 크게 해본다
        if tmp < 0:
            left += 1
        # 만약 양수라면 큰 값(right)을 더 작게 해본다
        elif tmp > 0:
            right -= 1
        else:
            print(*ans)
            sys.exit(0)

print(*ans)