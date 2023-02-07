# 문제
링크 : https://www.acmicpc.net/problem/1946
해결여부 : yes

# 코드
```
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    candi = [list(map(int, input().split())) for _ in range(n)]
    candi.sort(key= lambda x: x[0])
    
    cnt = 1
    min_rank = candi[0][1]
    for i in range(1, n):
        if candi[i][1] < min_rank:
            min_rank = candi[i][1]
            cnt += 1
    print(cnt)
```

# 문제 풀이
지원자들의 등수가 주어지고, 두 성적 모두 다른 어느 지원자보다 못한 지원자는 채용하지 않는다. 즉 `상위 호환` 인 지원자가 있으면 뽑히지 않는다.

우선 서류심사 등수를 가지고 오름차순 정렬한다. 맨 앞부터 서류심사 등수가 가장 높은 사람이 오게 된다.

그러면 뒤에 있는 사람들은 서류심사가 무조건 앞의 사람보다 낮으니, 채용되려면 본인 앞의 사람 중 최소한 가장 면접 등수가 낮은 사람보다는 면접 등수가 높아야 한다.

그러면, 지금까지 뽑힌 사람들 중 가장 면접 등수가 높은 사람의 등수를 변수에 저장해 두고, 그 변수보다 작은, 즉 등수가 높은 사람만 계속해서 채용하고, 또 그 등수로 변수를 갱신하고 한다면 `N`번만에 합격자를 골라낼 수 있다.

시간 복잡도는 정렬에 사용된 `NlogN`일 것이다.

# 부족했던 점

# 마무리