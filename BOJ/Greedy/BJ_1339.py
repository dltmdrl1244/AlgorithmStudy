import sys

n = int(sys.stdin.readline())

alpha = []
alpha_dict = {}
numList = []

for i in range(n):
    alpha.append(sys.stdin.readline())

for i in range(n):
    for j in range(len(alpha[i])):
        if alpha[i][j] in alpha_dict:
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1) 
        else:
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

for val in alpha_dict.values(): # dict에 저장된 수들을 모두 리스트에 추가
    numList.append(val)

numList.sort(reverse=True) # 수들을 내림차순 정렬

sum = 0
pows = 9
for i in numList: # 첫 번째 부터 가장 큰 부분을 차지하므로 9를 곱해준다
    sum += pows * i
    pows -= 1
# 내려갈수록 그 알파벳이 차지하는 비중이 적으므로 -1 
print(sum)