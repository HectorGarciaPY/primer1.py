while True:
	print("> Quants cops repeteix l'eco?")
	eco = int(input())
	print(">Què vols dir?:")
	word = input()
	print("")
	if word == "adeu" or word == "Adeu" or word == "ADEU":
		break
	else:	
		for i in range(eco):
			print(word)
	
