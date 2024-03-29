# 문제
링크 : [3020 개똥벌레](https://www.acmicpc.net/problem/3020)

해결여부 : yes

# 문제 풀이
> 누적합을 이용해서 해당 구간에서 부숴야 하는 종유석/석순을 더해간다.
- 길이가 4인 종유석은 4구간뿐 아니라 3구간, 2구간, 1구간에서도 부숴야 한다.
- 길이가 3인 종유석은 3구간뿐 아니라 2구간, 1구간에서도 부숴야 한다.
- 즉 길이가 긴 것부터 더 짧은 것에 더해간다.
- 종유석과 석순은 반대로 자라므로 각 구간에서 부숴야 하는 장애물을 계산할 때 서로 반대편 인덱스를 참조한다.

# 마무리
- 높이 제한과 장애물 개수가 매우 크므로 나이브하게 n*h로는 풀 수 없다