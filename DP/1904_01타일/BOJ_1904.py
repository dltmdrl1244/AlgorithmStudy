n = int(input())

temp1 = 1
temp2 = 2
temp3 = 0

if n == 1 :
    print(1)
    exit(0)
elif n == 2 :
    print(2)
    exit(0)

for i in range(3, n+1) :
    temp3 = temp1 + temp2 % 15746
    temp1 = temp2 % 15746
    temp2 = temp3
    
print(temp3 % 15746)
