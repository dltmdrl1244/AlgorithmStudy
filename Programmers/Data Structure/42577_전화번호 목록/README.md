# 문제
링크 : [42577 전화번호 목록](https://www.acmicpc.net/problem/42577)

해결여부 : yes

# 문제 풀이
- 모든 전화번호를 해쉬맵에 저장해 둔다
- 다시 한번 모든 전화번호를 탐색하는데 이 때는 앞에서부터 한 글자씩 살펴보며 해쉬에 존재하는 접두어가 있는지 검색한다.
- 예컨대 ABCDE 같은 문자열을 볼 때 A가 있는지 보고, AB가 있는지 보고... 이런식으로 하나씩 늘려가며 확인한다.
- 이 때 끝까지 가서 ABCDE 자기 자신을 보고 접두어라고 오판하지 않도록 `temp != numbers` 조건을 추가한다.

# 마무리
단순 key value 페어를 저장하는 기능이 아닌 set처럼 이용할 수도 있다