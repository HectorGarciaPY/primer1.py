def recogida():
	l=[]
	while True:
		l.append(int(input("Escribe un digito: ")))
		if len(l) > 1:
			break
	return l

def comparar(a,b):
	for i in a:
		for j in b:	
			if i == j:
				return "cierto"
	return "falso"

NumListas = int (input("¿Cuántas listas quieres comparar?"))
for var in range(NumListas):
	lista1=recogida()
	lista2=recogida()
	print(lista1,lista2)

print(comparar(lista1,lista2,))
