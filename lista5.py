lista1=list()
lista2=list()
dia=7
for i in range(6):
	dia=dia-1
	lista1.append(int(input("Temperatura maxima de hace "+str (dia)+" dias:")))
	lista2.append(int(input("Temperatura minima de hace "+str(dia)+" dias:")))
med=(sum(lista1)+sum(lista2))/len(lista1)+len(lista2)
print("La temperatura media de los seis dias ha sido de: ",round(med,2), " grados.")
print("La temperatura minima ha sido de: ",min(lista1+lista2)," grados.")
print("La temperatura maxima ha sido de: ",max(lista1+lista2)," grados.")