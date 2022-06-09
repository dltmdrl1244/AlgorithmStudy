import matplotlib.pyplot as plt

fin=open('input.txt', 'r')

n = int(fin.readline())
coord = []
for line in fin:
	coord.append(list(map(float, line.split())))

fout = open('output.txt','r')
fout.readline()
city = []
line = fout.readline()
city = list(map(int, line.split(',')))

ax = plt.gca()
plt.tight_layout()
for i in range(n):
	plt.scatter(coord[i][0], coord[i][1], color='black')

for i in range(len(city)-1):
	x = [coord[city[i]][0], coord[city[i+1]][0]]
	y = [coord[city[i]][1], coord[city[i+1]][1]]
	plt.plot(x, y, color='red')

plt.show()
