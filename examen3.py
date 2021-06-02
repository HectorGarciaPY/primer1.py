while True:
	print("Que temperatura hace?")
	temperatura=int(input())
	if temperatura<31 and temperatura>-11:
		if temperatura<0:
			print("Tienes que llevar Polar")
			break
		elif temperatura>-1 and temperatura<10:
			print("Tienes que llevar Guantes y Bufanda")
			break
		elif temperatura>9 and temperatura<20:
			print("Tienes que llevar manga corta")
			break
		elif temperatura>19:
			print("Tienes que llevar bañador")
			break
	else:
		print("Vuelve a intentarlo")
		continue				
