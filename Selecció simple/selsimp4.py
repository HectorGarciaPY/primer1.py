print("Pon los numeros de tu DNI y te dire la letra:")
x=int(input())
b=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
print("Tu DNI es:",x,b[x%23])