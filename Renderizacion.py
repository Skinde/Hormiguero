def renderizacion():  # PONGAN SU CODIGO AQUI ESTO SE EJECUTA EN UN BUCLE
	#Dibujo de la hormiga 
	for d in range(len(hormigas)):
		dibujar_rectangulo(negro, hormigas[d][0], hormigas[d][1], 1, 1)
	#Actualizacion de la ventana
	pygame.display.flip()
	pantalla.fill((120, 200, 80))


	
