# 문제
링크 : [20310 타노스](https://www.acmicpc.net/problem/20310)

해결여부 : yes

# 문제 풀이
> 쉬운 그리디
- 0과 1을 적절히 지워서 사전순으로 가장 앞서는 문자열을 만든다.
- 0이 1보다 사전순으로 앞서므로, 최대한 앞의 0을 살려야 하고, 반대로 앞의 1은 최대한 제거해야 한다.
- 즉 1을 지울 때는 앞에서부터, 0을 지울 때는 뒤에서부터 지운다.
- 뒤에서부터 찾을 때는 `rfind` 함수를, 지울 때는 `erase` 함수를 사용하면 쉽다.

# 마무리
C++의 string 함수들을 많이 알아두면 문제 난이도가 확 내려가는 것 같다.