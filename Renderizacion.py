def renderizacion():  # PONGAN SU CODIGO AQUI ESTO SE EJECUTA EN UN BUCLE

	#Logo de inicio
	if fase_dejuego == 0: 
		dibujar(Utec, 285, 140)
		pygame.display.flip()   
		time.sleep(2)
	pantalla.fill((81, 209, 246))

	#Dibujo de el mapa
	for n in range(450): 
		for x in range(800):
			if mapa[n][x] == 1:
				dibujar_rectangulo((78,59,49),x,n+50,1,1)

	#Dibujo de la hormiga reina
	dibujar(hormiga_reina,hormigax,hormigay) 

	#Actualizacion de la ventana
	pygame.display.flip() 
	pantalla.fill((81, 209, 246))

	
