# 문제
링크 : [15686 치킨 배달](https://www.acmicpc.net/problem/15686)

해결여부 : Y

# 문제 풀이
> 조합으로 치킨집을 선정하고 msBFS 수행
- 여러 치킨집들 중 선택할 m개 치킨집 말고는 모두 폐업함
- 모든 치킨집을 0으로 표시하고 선택한 m개를 조합으로 선택하여 치킨집을 선정
- 그 이후 큐에 모든 치킨집의 위치를 넣고 BFS를 수행, 거리 정보 저장
- 탐색 중 집을 발견하면 거리를 추가하여 모든 집의 거리를 리턴
- 벽이나 다른 이동의 제약조건이 없으므로 방문여부만 체크해줌

# 마무리
X