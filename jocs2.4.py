import random
while True:
	maquina=random.randint(0,3)
	print("Cuantas piedras crees que saldran?")
	suposicion=int(input())
	if suposicion<7 and suposicion>0:
		print("Cuantas piedras tienes tu en la mano?")
		jugador=int(input())
		if jugador<4 and suposicion>0:
			x=maquina+jugador
	if x==suposicion:
		print("Has ganado, la suma ha salido:",x)
	else:
		print("Has perdido, la suma ha salido:",x)
	print("")	
	print("Quieres volver a jugar? si o no")
	z=input()
	if z=="si":
		print("")
		continue
	elif z=="no":
		print("Vale, hasta la proxima.")
		break
	else:
		print("No te he entendido, hasta la proxima.")
		break			
			
		