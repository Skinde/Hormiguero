def renderizacion():
	if fase_dejuego == 0:
		dibujar(Utec, 285, 140)
		pygame.display.flip()
		time.sleep(2)
		pantalla.fill(blanco)
	if fase_dejuego == 1: 
		for n in range(450):
			for x in range(800):
				if mapa[n][x] == 1:
					dibujar_rectangulo((78,59,49),x,n+50,1,1)

	pygame.display.flip() #Actualiza la pantalla
