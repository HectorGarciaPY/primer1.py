import random
while True:
	print("Bienvenido, escoge un luchador para jugar:")
	print("1)Son Goku \n2)Jakie Chun \n3)Krilin \n4)Tenshinhan")
	x=int(input())
	y=random.randrange(0,80)
	if x==1:
		s=random.randrange(80,90)
		print("Atacas con una fuerza de:", s)
		if y>s:
			print("Has perdido, Mr. Satan ha atacado con una fuerza de:",y)
		elif y==s:
			print("Has empatado.")
		elif y<s:
			print("Has ganado, Mr.Satan solo tenia una fuerza de:",y)
	if x==2:
		j=random.randrange(50,80)
		print("Atacas con una fuerza de:", j)
		if y>j:
			print("Has perdido, Mr. Satan ha atacado con una fuerza de:",y)
		elif y==j:
			print("Has empatado.")	
		elif y<j:
			print("Has ganado, Mr.Satan solo tenia una fuerza de:",y)			
	if x==3:
		k=random.randrange(20,50)
		print("Atacas con una fuerza de:", k)
		if y>k:
			print("Has perdido, Mr.Satan ha atacado con una fuerza de:",y)
		elif y==k:
			print("Has empatado.")	
		elif y<k:
			print("Has ganado, Mr.Satan solo tenia una fuerza de:",y)
	if x==4:
		t=random.randrange(20,50)
		print("Atacas con una fuerza de:", t)
		if y>t:
			print("Has perdido, Mr.Satan ha atacado con una fuerza de:",y)
		elif y==t:
			print("Has empatado.")	
		elif y<t:
			print("Has ganado, Mr.Satan solo tenia una fuerza de:",y)
	else:
		print("No te he entendido")		
	print("----------")
	print("¿Quieres seguir jugando?")
	print("¿si o no?")
	h=input()
	if h=="si":
		print("Perfecto")
		print("----------")
	elif h=="no":
		print("Hasta la proxima.")
		break
	else:
		print("No te he entendido.")
		print("¿Quieres seguir jugando?")
		print("¿si o no?")
		o=input()
		if o=="si":
			print("Perfecto")
			print("----------")
		elif o=="no":
			print("Hasta la proxima.")
			break
		else:
			print("No te he entendido.")	




