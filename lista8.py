y=list()
for i in range (5):
	x=list()
	for j in range(10):
		if i==0 or i==4:
			x.append("1")
		elif j==0 or j==9:
			x.append("1")
		else:
			x.append("0")
	y.append(x)
	print(x)		
