def juego(): #PONGAN SU CODIGO AQUI ESTO SE EJECUTA EN UN BUCLE
	for d in range(len(hormigas)):
		if mapa[hormigas[d][1]][hormigas[d][0]] < 1:
		    mapa[hormigas[d][1]][hormigas[d][0]] += 0.01
	if fase_dejuego != 0:
		#Decide en que direccion van las hormigas
		for r in range(len(hormigas)):
			del calculadora[:]
			for l in range(len(verdosidad[r])):
				f = random.randint(0,1)
				calculadora.append(f*verdosidad[r][l])
			#Si se han elegido valores random iguales decide aleatoriamente entre estos
			jo = uwu(calculadora)
			#actualiza su pocision
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
		#si cogen comida eliminan la comida del mapa
	if fase_dejuego !=0:
		try:
			for le in range(len(hormigas)):
				for li in range(len(comida)):
					if hormigas[le][0] == comida[li][0] and hormigas[le][1]==comida[li][1]:
						comida.remove([comida[li][0],comida[li][1]])
						hormigas[le][2]=1
		except:
			hola = 0
	#Si se salen del borde las devuelve al centro
	for bordero in range(len(hormigas)):
		if hormigas[bordero][0] == 999 or hormigas[bordero][1] == 999 or hormigas[bordero][0] == 1 or hormigas[bordero][1] == 1:
			hormigas[bordero][0] = 400
			hormigas[bordero][1] = 250
			historial[bordero] = []
			hormigas[bordero][2] = 0

		for i in range(len(hormigas)):
			if(hormigas[i][2]==0):
				historial[i].append(hormigas[i][:2])
			#Cuando llega la colonia entrega la colonia y se elimina su historial 
			else:
				for o in range(len(historial[i])-1,0,-1):
					hormigas[i][0]=historial[i][o][0]
					hormigas[i][1]=historial[i][o][1]
				historial[i] = []
				hormigas[i][2] = 0
				
				
		
