# 문제
링크 : https://www.acmicpc.net/problem/11722
해결여부 : yes

# 코드
```
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * (n)

for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
```

# 문제 풀이
간단한 dp 문제이다.

2중 for문을 돌면서, 자신 앞에서 자기보다 큰 수를 발견할 때마다 그 dp값에 1을 더한 값을 비교하면서 더 큰 값으로 갱신 해준다.

그러면 결과적으로 `dp[i]`에는 i번째 수까지의 최장 부분 수열의 길이가 들어간다.
그리고 `dp` 리스트의 최댓값을 구한다.

# 부족했던 점

# 마무리