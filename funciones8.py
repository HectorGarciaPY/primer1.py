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

ListaGeneral=list()

NumListas = int (input("¿Cuántas listas quieres comparar?"))
for var in range(NumListas):
	ListaGeneral.append(recogida())

for i in range(len(ListaGeneral)):
	for j in range(i+1,len(ListaGeneral)):
		comparar(ListaGeneral[i],ListaGeneral[j])

