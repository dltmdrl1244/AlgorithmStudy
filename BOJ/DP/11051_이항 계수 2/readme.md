# 문제
링크 : https://www.acmicpc.net/problem/11051
해결여부 : yes

# 코드
```
n, k = map(int, input().split())

pascal = [[1] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(len(pascal[i-1]) - 1):
        pascal[i].append(pascal[i-1][j] + pascal[i-1][j+1])
    pascal[i].append(1)

print(pascal[n][k] % 10007)
```

# 문제 풀이
이항 계수를 푸는 간단한 문제로 파스칼의 삼각형을 이용해서 만들 수 있다.
파스칼의 삼각형은 바로 위의 두 숫자의 합이 아래 칸에 적히므로 이를 활용해서 리스트에 append 해주는 식으로 동적으로 구현하였다.

# 부족했던 점


# 마무리
`from itertools import combinations` 을 활용하여 조합을 쉽게 구할 수 있다. 다만 메모리 초과를 염두해야 한다.