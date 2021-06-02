file = open('trabajadores.csv', 'r').readlines()
TrabajadoresGeneral = []

def lecturaArchivos(file):
	fichero=open(file,"r")
	for fila in fichero:
		posicionComa=0	
		Trabajador=[]
		for i in range(len(fila)):
			if fila[i]==",":
				Trabajador.append(fila[posicionComa:i])
				posicionComa=i+1	
		Trabajador.append(fila[posicionComa:-1])
		TrabajadoresGeneral.append(Trabajador)


def ConvertirAnumeros():
	for i in TrabajadoresGeneral:
		for j in range(len(i)):
			try:
				i[j]=int(i[j])
			except:
				pass

def SueldoMedio():
	SueldoMedio=0
	for Trabajador in TrabajadoresGeneral:
		SueldoMedio=SueldoMedio+Trabajador[5]
	SueldoMedio=SueldoMedio/len(TrabajadoresGeneral)
	print("El sueldo medio es: "+str(SueldoMedio))

def funciones():
	Empleados=0
	Vendedores=0
	Analistas=0
	Directores=0
	Presidentes=0
	for i in TrabajadoresGeneral:
			if i[2]=="EMPLEADO":
				Empleados=Empleados+1
			if i[2]=="VENDEDOR":
				Vendedores=Vendedores+1
			if i[2]=="ANALISTA":
				Analistas=Analistas+1
			if i[2]=="DIRECTOR":
				Directores=Directores+1
			if i[2]=="PRESIDENTE":
				Presidentes=Presidentes+1
	fichero1=open("funciones.txt","w")
	fichero1.write("Empleados: "+str(Empleados)+"\nVendedores: "+str(Vendedores)+"\nAnalistas: "+str(Analistas)+"\nDirectores: "+str(Directores)+"\nPresidentes: "+str(Presidentes))



lecturaArchivos("trabajadores.csv")
ConvertirAnumeros()
print(TrabajadoresGeneral)
SueldoMedio()
funciones()