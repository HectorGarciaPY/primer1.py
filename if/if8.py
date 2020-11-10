import calendar
d=int(input("Dime un dia:"))
m = int(input("Dime un mes:(numero)"))
a=int(input("Dime un año:"))
if a >=0:
  if m == 1 or m==3 or m == 5 or m==7 or m == 8 or m==10 or m == 12:
    if d>=1 and d<=31:
      print("Es correcta!")
    else:
      print("Es incorrecta...")
  elif m== 4 or m == 6 or m==9 or m == 11:
    if d>=1 and d<=30:
      print("Es correcta!")
    else:
      print("Es incorrecta...")
  elif m== 2:
    if calendar.isleap(a):
      if d>=1 and d<=29:
        print("Es correcta!")
      else:
        print("Es incorrecta...")  
    elif not calendar.isleap(a):
      if d>=1 and d<=28:
        print("Es correcta!")
      else:
        print("Es incorrecta...")
  else:
    print("Es incorrecta...")
else:
  print("Es incorrecta...")             