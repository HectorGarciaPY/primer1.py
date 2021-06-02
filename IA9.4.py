def comptarPurina(adn):
	cops=0
	for i in range(len(adn)):
		if adn[i]=="G" and adn[i+1]=="A":
			cops=cops+1
	return cops

adn = ["A","A","A","G","A","A","A","G","T","C","T","G","A","C","T","C","T","G","A","C"]

print("Hi ha purina ",(comptarPurina(adn)), " cops")
