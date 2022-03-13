<<<<<<< HEAD
n = int(input())

sum = [0 for _ in range(301)]
score = [0 for _ in range(301)]
for i in range(n) :
    score[i] = int(input())
    
sum[0] = score[0]
sum[1] = score[0] + score[1]
sum[2] = max(score[1], score[0]) + score[2]

for i in range(3, n) :
    sum[i] = max(sum[i-2], sum[i-3] + score[i-1]) + score[i]
    
    
print(sum[n-1])
=======
n = int(input())

sum = [0 for _ in range(301)]
score = [0 for _ in range(301)]
for i in range(n) :
    score[i] = int(input())
    
sum[0] = score[0]
sum[1] = score[0] + score[1]
sum[2] = max(score[1], score[0]) + score[2]

for i in range(3, n) :
    sum[i] = max(sum[i-2], sum[i-3] + score[i-1]) + score[i]
    
    
print(sum[n-1])
>>>>>>> 2cca8c74017864ad199593fcee09d7b03802337d
