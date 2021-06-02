puntuacion=0
contador=0
while True:
	print("Escribe un nombre divertido:")
	x=input()
	v1=x[:3]
	if x[0].isnumeric() and x[(len(x)-1)].isnumeric() and x[1].isnumeric() and x[(len(x)-2)].isnumeric() and x[2].isnumeric() and x[(len(x)-3)].isnumeric():
		if x[0]==x[(len(x)-1)] and x[1] == x[(len(x)-2)] and x[2]==x[(len(x)-3)] and x[3] == x[(len(x)-4)]:
			print("Capicua de lletres plus +4")
	elif x[0].isnumeric() and x[(len(x)-1)].isnumeric() and x[1].isnumeric() and x[(len(x)-2)].isnumeric():
			if x[0]==x[(len(x)-1)] and x[1] == x[(len(x)-2)]:
				print("Capicua numèric normal +2")
				puntuacion=puntuacion+2	
	elif x[0]==x[(len(x)-1)] and x[1] == x[(len(x)-2)] and x[2]==x[(len(x)-3)] and x[3] == x[(len(x)-4)] and x[4] == x[(len(x)-5)] and x[5]==x[(len(x)-6)]:
		print("Supernom divertit!!! +5")
		puntuacion=puntuacion+5			
	elif x[0]==x[(len(x)-1)] and x[1] == x[(len(x)-2)] and x[2]==x[(len(x)-3)] and x[3] == x[(len(x)-4)]:
		print("Capicua de lletres plus +4")
		puntuacion=puntuacion+4
	elif x[0]==x[(len(x)-1)] and x[1] == x[(len(x)-2)]:
		print("Capicua de lletres +3")
		puntuacion=puntuacion+3
	elif x[0]!=x[(len(x)-1)] or x[1] != x[(len(x)-2)]:
		print("Ets un avorrit, el nom no mola")
		contador=contador+1
		if contador==2:
			print("No tens gens d'originalitat. No pots tenir gos, no pots sortir al carrer.\n""Adéu!")
			break