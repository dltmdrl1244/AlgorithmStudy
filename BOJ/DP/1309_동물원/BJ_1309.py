n = int(input())
a = 3
b = 7
c = 0

if n == 1 :
    print(3)
elif n == 2 :
    print(7)
else :
    for i in range(2, n) :
        c = 2 * b + a
        a = b
        b = c

    print(c % 9901)