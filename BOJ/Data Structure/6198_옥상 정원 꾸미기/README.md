# 문제
링크 : [6198 옥상 정원 꾸미기](https://www.acmicpc.net/problem/6198)

해결여부 : yes

# 문제 풀이
- 오큰수와 비슷한 매커니즘으로 오른쪽에서부터 살펴보며 스택에 넣었다 뺐다의 과정을 반복
- 아래로 내려다볼 수 있는 카드들을 세야 하기 때문에 함부로 스택에서 빼면 안 됨
- 대신 '이 빌딩에서 내려다볼 수 있는 빌딩 수' 즉 정답 배열에 녹여냄으로써 그 정보를 보존 가능
- 지금 빌딩이 스택에 들어 있는 빌딩보다 크다 -> 이 빌딩을 내려다볼 수 있다 -> 이 빌딩에서 내려다볼 수 있는 빌딩들까지 볼 수 있다
- 즉 그 빌딩에서 볼 수 있는 빌딩의 수에 1을 더한 값을 더해 나간다.

# 마무리
