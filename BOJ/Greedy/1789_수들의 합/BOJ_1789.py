a = int(input())
s = 0
cnt = 0
while True:
    if s + cnt > a:
        print(cnt-1)
        break
    s += cnt
    cnt += 1