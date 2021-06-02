import random 
l = [[],[],[],[],[]]
for i in range(5):
	for a in range(5):
		l[i].append(random.randint(1,100))
	print(l[i])
d1 = []
d2 = []

for d in range(5):
	d1.append(l[d][d])

x=4
y=0
for h in range(5):
  d2.append(l[y][x])
  x=x-1
  y=y+1

print("La suma de la diagonal es: " , sum(d1))
print("La suma de la diagonal inversa es: ", sum(d2))
