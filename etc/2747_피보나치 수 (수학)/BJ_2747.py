n = int(input())

a = 1
b = 1
c = 0

if n in (1,2) :
    print(1)
else :
    for i in range(2, n) :
        c = a + b
        a = b
        b = c

    print(c)