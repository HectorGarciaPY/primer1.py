lista=[x for x in range(1000, 2001)]
for i in (lista):
	if i==2000:
		print(i,end="")
	else:
		print(i,"+",end="",sep="")
print("=",sum(lista))



