import random
while True:
	print("Hola, escoge:\n1) Piedra\n2) Papel\n3) Tijeras")
	q=int(input())
	a=11
	x=random.randint(1,3)
	if q==1 and x==3:
		print("Has Ganado!, la maquina ha sacado:",x)
	elif q==1 and x==2:
		print("Has perdido..., la maquina ha sacado:",x)
	elif q==2 and x==1:
		print("Has Ganado!, la maquina ha sacado:",x)
	elif q==2 and x==3:
		print("Has perdido...la maquina ha sacado:",x)
	elif q==3 and x==1:
		print("Has perdido...la maquina ha sacado",x)	
	elif q==3 and x==2:
		print("Has Ganado!, la maquina ha sacado:",x)
	elif q==x:
		print("Has empatado!la maquina ha sacado:",x)
	else:
		print("No te he entendido.")	
	print("Quieres volver a jugar? si(1) o no(2):")
	z=int(input())
	if z==1:
		print("")
		continue
	elif z==2:
		print("Vale, hasta la proxima.")
		break	
						

