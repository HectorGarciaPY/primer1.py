y=0
j=0
lista=list()
for i in range (5):
	print("Dime el nombre, apellido, edad, altura y peso:")
	x=input()
	lista.append(x)
print(lista)
cadena = " ".join(lista)
t=cadena.count("a")
p=cadena.count("A")
u=t+p
o=cadena.count("9")
print("Numero de A:",u)
print("Numero de 9:",o)