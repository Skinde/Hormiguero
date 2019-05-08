def renderizacion():  # PONGAN SU CODIGO AQUI ESTO SE EJECUTA EN UN BUCLE
	if fase_dejuego == 0: #Logo de inicio
		dibujar(Utec, 285, 140)
		pygame.display.flip()   
		time.sleep(2)
	pantalla.fill((81, 209, 246))

	for n in range(450): #Dibujo de el mapa
		for x in range(800):
			if mapa[n][x] == 1:
				dibujar_rectangulo((78,59,49),x,n+50,1,1)

	dibujar(hormiga_reina,hormigax,hormigay) #Dibujo de la hormiga reina
	pygame.display.flip() #Actualizacion del codigo
	pantalla.fill((81, 209, 246))

	
