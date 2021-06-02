def checkUpper(text):
	nouText=""
	for i in range(len(text)):
		if text[i]==".":
			print(text[i+1])
			nouText=nouText+text[i]
			nouText=nouText+text[i+1].upper()
			i=i+1
		else:
			nouText=nouText+text[i]
	return nouText

text=input("Entra el text: ")
print(checkUpper(text))
