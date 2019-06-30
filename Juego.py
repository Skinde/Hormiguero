def juego(): #PONGAN SU CODIGO AQUI ESTO SE EJECUTA EN UN BUCLE
	for d in range(len(hormigas)):
		if mapa[hormigas[d][1]][hormigas[d][0]] < 1:
		    mapa[hormigas[d][1]][hormigas[d][0]] += 0.01
	if fase_dejuego != 0:
		for r in range(len(hormigas)):
			del calculadora[:]
			for l in range(len(verdosidad[r])):
				f = random.randint(0,1)
				calculadora.append(f*verdosidad[r][l])
			jo = calculadora.index(max(calculadora))
			print("pipo")
			if jo == 0:
				hormigas[r][0] -= 1
				hormigas[r][1] += 1
			if jo == 1:
				hormigas[r][1] += 1
			if jo == 2:
				hormigas[r][0] += 1
				hormigas[r][1] += 1
			if jo == 3:
				hormigas[r][0] -= 1
			if jo == 4:
				hormigas[r][0] += 1
			if jo == 5:
				hormigas[r][0] -= 1
				hormigas[r][1] -= 1
			if jo == 6:
				hormigas[r][1] -= 1
			if jo == 7:
				hormigas[r][0] += 1
				hormigas[r][1] -= 1
		
