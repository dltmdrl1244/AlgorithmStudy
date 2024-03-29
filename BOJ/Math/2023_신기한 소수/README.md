# 문제
링크 : [2023 신기한 소수](https://www.acmicpc.net/problem/2023)

해결여부 : yes

# 문제 풀이
- 한 수 안에서 소수 판별해야 하는 수가 여러 수이다
- 리스트에 True False로 기록하는 방법이 담백하고 빠르지만 범위가 1억까지이므로 메모리 초과가 발생한다. 따라서 모든 소수에 대해서 사전에 구해 놓을 수는 없음
- 하나 확실한 것은 첫 번째 자릿수 역시 소수여야 하므로 한 자릿수 소수인 2, 3, 5, 7로 시작해야 한다는 것
- 나머지 수에 대해서는 시도하지 않음으로써 시행 횟수를 4/10으로 줄일 수 있다
- 소수 뒤에 0부터 9까지의 숫자를 붙여보고, 그 수 역시 소수이면 동일 함수를 재귀 호출함으로써 백트래킹 내지는 DFS 형식으로 소수를 찾아 나간다
- 자연스럽게 정렬도 가능하고 백트래킹 가지치기가 가능하므로 속도도 빠르다

# 마무리