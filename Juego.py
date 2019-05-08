def juego(): #PONGAN SU CODIGO AQUI ESTO SE EJECUTA EN UN BUCLE

	#Se ejecuta cuando el programa empieza
	if fase_dejuego == 0: 
		# se declara posicion (x,y) de la hormiga
		global hormigax 
		global hormigay 
		hormigax = 100
		hormigay = 45
		
	#Generacion de numeros aleatorios
	movex = random.randint(0, 2) 
	movey = random.randint(0, 2)

	#Movimiento de la hormiga
	if movex == 0: 
		hormigax -= 5
	if movex == 2:
		hormigax += 5
	if movey == 0 and hormigay > 45:
		hormigay -= 5
	if movey == 2:
		hormigay += 5





