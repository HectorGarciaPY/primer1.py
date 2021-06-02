def comptarLletra(adn,lletra):
	cops=0
	for i in adn:
		if i==lletra:
			cops=cops+1
	return cops

adn=["A","A","A","G","A","A","A","G","T","C","T","G","A","C","T","C","T","G","A","C"]
lletra = input("Entra la lletra que vols comptar: ").upper()

print(comptarLletra(adn,lletra))

