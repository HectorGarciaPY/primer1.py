import random 
l=[[],[],[],[],[]]
for i in range(5):
	for ii in range(5):
		l[i].append(random.randint(0,100))
	print(l[i])

print()
print(l)