contador=0
while True:
	print("Escribe un nombre divertido:")
	x=input()
	if x[0]==x[(len(x)-1)] and x[1] == x[(len(x)-2)]:
		print("Es un nom divertit")
	else:
		print("Ets un avorrit, el nom no mola")
		contador=contador+1
		if contador==2:
			print("No tens gens d'originalitat. No pots tenir gos, no pots sortir al carrer.\n"" Adéu!")
			break
	

