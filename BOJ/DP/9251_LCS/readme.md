# 문제
링크 : https://www.acmicpc.net/problem/9251
해결여부 : no

# 코드
```
import sys
input = sys.stdin.readline

str1 = list(input().strip())
str2 = list(input().strip())
len1 = len(str1)
len2 = len(str2)

dp = [[0] * 1001 for _ in range(1001)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[len1][len2])
```

# 문제 풀이
각 단어의 길이만큼 2차원 표를 만든다.
DP는 2차원 배열로 사용하고, `dp[i][j]` 는 단어1의 i번째 글자까지, 단어2의 j번째 글자까지의 LCS를 나타낸다.
그렇다면 `dp[i][j]`는 단어1의 i번째 글자과 단어2의 j번째 글자가 같은지 여부에 따라 다를 것이다.

만약 같다면, `dp[i-1][j-1]`에 이미 한 글자 전까지의 최댓값이 들어있을 것이고, 그 값보다 1이 커진 값이므로 +1 해준 값을 저장한다.

만약 다르다면 값이 이전보다 커질 수는 없다. 그래서 이전 최댓값을 그대로 가져온다. `dp[i-1][j]`와 `dp[i][j-1]` 중에서 큰 값을 선택한다.

그렇게 표를 모두 채운 후에 `dp[len1][len2]` 를 출력하면 된다.

# 부족했던 점
이전 알고리즘 수업시간에 편집 거리 알고리즘을 배운 적이 있어서 이와 관련하여 2차원 표를 만드는 것까지는 생각을 했는데, 점화식을 잘못 세워서 `XXXXXF`와 `XFXXXQ` 와 같은 케이스에서 `XXX`와 `XFX`, 즉 `dp[3][3]`에서 이전 `dp[2][3]` 값인 2에서, word1[3]과 word2[3]이 같으므로 1을 증가시켜주게끔 하였더니 단어 길이보다 더 커지는 경우가 발생해서 이를 보완하고자 했는데, 생각이 잘 나지 않아 구글링을 하였는데, 의외로 너무 단순하고 직관적이었다.

# 마무리
너무 복잡하게 생각해서 오히려 미궁에 빠졌던 게 아닐까... 단순하게 생각하자..!