# 문제
링크 : https://www.acmicpc.net/problem/16194
해결여부 : yes

# 코드
```
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dp = [float('inf')] * 1001
dp[0] = 0

for i in range(1, n+1):
    for j in range(i):
        dp[i] = min(dp[i], dp[j] + cards[i-j-1])

print(dp[n])
```

# 문제 풀이
`카드 n장을 가장 싸게 사는 방법`은 다음과 같다.
- `카드 0장을 가장 싸게 사는 방법` + n개짜리 카드팩의 가격
- `카드 1장을 가장 싸게 사는 방법` + n-1개짜리 카드팩의 가격
- `카드 2장을 가장 싸게 사는 방법` + n-2개짜리 카드팩의 가격
  ...
- `카드 n-1장을 가장 싸게 사는 방법` + 1개짜리 카드팩의 가격

카드팩의 가격은 `cards` 리스트에 저장해 놓았고, 반복되는 `가장 싸게 사는 방법` 을 dp로 사용하여 점화식을 세울 수 있다.

`dp[i]`당, 이전까지의 모든 경우의 수를 고려하여 `i-1`번 비교한다.
시간 복잡도는 `N^2` 이다.

# 부족했던 점

# 마무리