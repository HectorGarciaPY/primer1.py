def contar(a,c):
	j=0
	for l in range(c):
		b=input("Que quieres que cuente: ")
		for i in a:
			if i==b:
				j=j+1
			return "Numero de",b,j,":"
a=input("Pon una oración\n")
c=int(input("Cuantas grafias quieres contar?"))
print(contar(a,c))

	