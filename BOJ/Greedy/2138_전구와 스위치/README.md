# 문제
링크 : [2138 전구와 스위치](https://www.acmicpc.net/problem/2138)

해결여부 : no

# 문제 풀이
- 이거 켜면 저거 꺼지고 저거 키면 이거 꺼지고 굉장히 복잡하기 때문에, 앞에서부터 차근차근 처리
- 포인트는 N번째가 지나가면 N-1번째의 전구는 그 상태가 변하지 않는다. 즉 N번째에서 N-1번째의 전구를 책임져야 하고, 그 와중에 N번째가 바뀌면 N+1번째가 해결하도록 하고 넘어간다
- 첫 번째 전구의 경우 켜고 끄고가 경우의수가 모두 가능하지만 그 이후로는 모두 이전 행동에 종속된 행동을 할 수밖에 없다 (예를 들어 첫번째 전구가 켜져있어야 하는데 꺼져있다면, 두번째 스위치는 '반드시' 눌러야 하며, 반대로 전구가 켜져있어야 하고 커져 있다면 '반드시' 누르지 않아야 하기 때문.)
- 그러면 마지막 전구가 목표 상태와 달라질수가 있는데 그러면 그건 첫번째 전구의 시행이 잘못된 것. 만약 첫번째 전구의 두가지 경우의 수가 모두 실패한다면 불가능한 시행.

# 마무리
퍼즐 푸는것처럼 각 버튼을 여러번 딸깍딸깍 할 수 있다고 생각했고, on/off 하는 스위치이니까 각 버튼을 한 번씩 누른다/안 누른다로 나뉘는거라고 생각을 못했다.. 왜 이걸 생각못했을까