print("Escribe cualquier cosa y le dare la vuelta:")
x=input()
for i in range (0,(len(x))):
	y=len(x)-i-1
	print(x[y],end="")