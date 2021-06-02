file = open('world.csv', 'r').readlines()
countrylist = []

for i in file:
	i = i.replace('"', '')
	countrylist.append(i.split(','))
	#print(i)

def ConvertirAnumeros():
	for i in countrylist:
		for j in range(len(i)):
			#print(i[j])
			try:
				i[j]=float(i[j])
			except:
				pass

#def Escoger():
#	x=input("¿Quieres saber un pais o un continente?: (1-->Pais o 2-->Continente)")
	
#	if x==1 :
#		QuequieresSaber()
#	elif x==2:
#		PaisesContinente()


def QuequieresSaber():
	x=input("¿Que país quieres consultar?:\n")
	j=input("¿Quieres verlo en pantalla o crear un archivo con los datos?: (1-->Pantalla o 2-->Archivo)")
	if j=="1":
		for i in countrylist:
			if x==i[1]:
				print("\nCodigo: ",i[0],"\nPais: ",i[1],"\nContinente: ",i[2],"\nRegion: ",i[3],"\nSuperficie: ",i[4],"\nAño de Independencia: ",i[5],"\nPoblación: ",i[6],"\nEsperanza de vida: ",i[7],"\nPIB: ",i[8],"\nPIB antiguo: ",i[9],"\nNombre Local: ",i[10],"\nForma de gobierno: ",i[11],"\nJefe de Estado: ",i[12],"\nCapital: ",i[13],"\nCodigo 2: ",i[14])
	if j=="2":
		for i in countrylist:
			if x==i[1]:
				fichero1=open(x+".txt","w")
				fichero1.write("\nCodigo: "+str(i[0])+"\nPais: "+str(i[1])+"\nContinente: "+str(i[2])+"\nRegion: "+str(i[3])+"\nSuperficie: "+str(i[4])+"\nAño de Independencia: "+str(i[5])+"\nPoblación: "+str(i[6])+"\nEsperanza de vida: "+str(i[7])+"\nPIB: "+str(i[8])+"\nPIB antiguo: "+str(i[9])+"\nNombre Local: "+str(i[10])+"\nForma de gobierno: "+str(i[11])+"\nJefe de Estado: "+str(i[12])+"\nCapital: "+str(i[13])+"\nCodigo 2: "+str(i[14]))
			

def PaisesContinente():
	x=input("¿Que continente quieres consultar?:\n")
	j=input("¿Quieres verlo en pantalla o crear un archivo con los datos?: (1-->Pantalla o 2-->Archivo)")
	pob=0
	sur=0
	if j=="1":
		print("Paises: ")
		for i in countrylist:
		 if x==i[2]:
				print(i[1])
				pob=pob+int(i[6])
				sur=sur+int(float(i[4]))
		print("Poblacion total: ", pob)
		print("Area total: ",sur)	

	if j=="2":
		paises=""
		for i in countrylist:
			if x==i[2]:
				pob=pob+int(i[6])
				sur=sur+int(float(i[4]))
				paises=paises+"\n"+str(i[1])	
				fichero1=open(x+".txt","w")
				fichero1.write("Continente: " + x + "\n" + "Paises: "+ paises + "\n" + "Poblacion: " + str(pob) + "\n" + "Superficie: " + str(sur)) +"km²"
				fichero1.close()

def EsperanzadeVida():
	x=float(input("¿Cual es la renta per capita que buscas?\n"))
	y=float(input("¿Y la esperanza de vida?\n"))
	j=input("¿Quieres verlo en pantalla o crear un archivo con los datos?: (1-->Pantalla o 2-->Archivo)\n")
	aaa=True
	f=0
	if j=="2":
		for i in countrylist:
			f=0
			try:
				f="{:.2f}".format(i[8]/i[6])
			except:
				f=0
			if x>=float(f):
				try:
					k=float(i[7])
					
				except:
					k=0
				if k==y:
					aaa=False
					fichero1=open("EsperanzaDeVida.txt","w")
					fichero1.write("El pasi que buscas es:\n", i[1])
					fichero1.close()
			if aaa:
				fichero1=open("EsperanzaDeVida.txt","w")
				fichero1.write("No se ha encontrado ningún país que tenga una renta per cápita de "+str(x),"y una esperanza de vida de "+str(y))
				fichero1.close()

				

	if j=="1":
		for i in countrylist:
			f=0
			try:
				f="{:.2f}".format(i[8]/i[6])
			except:
				f=0
			if x>=float(f):
				try:
					k=float(i[7])
					
				except:
					k=0
				if k==y:
					aaa=False
					print(i[1])	
	
		if aaa:
			print("No se ha encontrado ningún país que tenga una renta per cápita de "+str(x),"y una esperanza de vida de "+str(y))
#print(countrylist)
#Escoger()
#QuequieresSaber()
ConvertirAnumeros()
#QuequieresSaber()
#print(countrylist)
EsperanzadeVida()