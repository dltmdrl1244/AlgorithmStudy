# 문제
링크 : [1038 감소하는 수](https://www.acmicpc.net/problem/1038)

해결여부 : yes

# 문제 풀이
- 감소하는 수 -> 역으로 마지막 수보다 더 큰 수만 붙여 나간다
- 그리고 여러 수 중 가장 작은 수부터 찾아야 하므로 힙을 사용한다.
- 감소하는 수는 유한하며, 1022개이다. 1023개부터는 코드를 수행하지도 않고 -1을 출력해도 된다.

# 마무리