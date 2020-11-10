print("Selecciona el tipo de conversion:")
print("a) Km a millas marinas")
print("b) Km a millas terrestres")
print("c) Millas marinas a Km")
print("d) Millas marinas a Millas terrestres")
print("e) Millas terretres a Km")
print("f) Millas terrestres a millas marinas")
print("(Escribe a b c d e o f) ")
a=input()
if a=="a":
  print("Que cantidad quieres convertir?")
  x=int(input("KM:"))
  print("Millas marinas:", round(x/1.852, 3))
elif a=="b":
  print("Que cantidad quieres convertir?")
  x=int(input("Km:"))
  print("Millas terrestres:", round(x/1.609, 3))
elif a=="c":
  print("Que cantidad quieres convertir?")
  x=int(input("Millas marinas:"))
  print("Km:", round(x*1.852, 3))
elif a=="d":
  print("Que cantidad quieres convertir?")
  x=int(input("Millas marinas:"))
  print("Millas terrestres:", round(x*1.151, 3))
elif a=="e":
  print("Que cantidad quieres convertir?")
  x=int(input("Millas terrestres:"))
  print("Km:", round(x*1.609, 3))
elif a=="f":
  print("Que cantidad quieres convertir?")
  x=int(input("Millas terrestres:"))
  print("Millas marinas:", round(x*1.151, 3))
else:
  print("No te he entendido, vuelve a intentarlo.")  