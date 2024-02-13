# 문제
링크 : [2251 물통](https://www.acmicpc.net/problem/2251)

해결여부 : yes

# 문제 풀이
> DFS
- 각 물병의 용량을 set에 집어넣고 방문처리 하면서 DFS
- 부을 수 있는 양은 `min(from물병의 물 양, to물병의 용량 - to물병의 물 양)`
- a가 비어 있고 c가 0이 아닐 때 ans set에 기록

# 마무리