def relacion(a,b):
	if a>b:
		return 1
	elif a<b:
		return -1
	elif a==b:
		return 0	
a=int(input("Escribe un numero:"))
b=int(input("Escribe un numero:"))
print("El resultado es:",relacion(a,b))