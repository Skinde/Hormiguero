def juego(): #PONGAN SU CODIGO AQUI ESTO SE EJECUTA EN UN BUCLE
	for x in range(len(hormigas)):
		if mapa[hormigas[x][1]][hormigas[x][0]] < 1:
			mapa[hormigas[x][1]][hormigas[x][0]] += 0.001
	del probabilidad[:]
	for x in range(len(verdosidad)):
		for d in range(len(verdosidad[x])):
			probabilidad.append(round(verdosidad[x][d]+mapa[hormigas[x][1]][hormigas[x][0]])/2)
	print(probabilidad)

#Se ejecuta cuando el empieza
