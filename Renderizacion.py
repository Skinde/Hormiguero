def renderizacion():  # PONGAN SU CODIGO AQUI ESTO SE EJECUTA EN UN BUCLE
	#Dibujo de la hormiga 
	for d in range(len(hormigas)):
		dibujar_rectangulo(negro, hormigas[d][0], hormigas[d][1], 1, 1)
	
	for n in range(20):
		probmovhor.append([pantalla.get_at((hormigas[n][0]-1, hormigas[n][0]+1))[1]/200,
                     pantalla.get_at(
                    (hormigas[n][0], hormigas[n][0]+1))[1]/200,
                    pantalla.get_at(
                    (hormigas[n][0]+1, hormigas[n][0]+1))[1]/200,
                    pantalla.get_at(
                    (hormigas[n][0]-1, hormigas[n][0]))[1]/200,
                    pantalla.get_at(
                    (hormigas[n][0]+1, hormigas[n][0]))[1]/200,
                    pantalla.get_at(
                    (hormigas[n][0]-1, hormigas[n][0]-1))[1]/200,
                    pantalla.get_at(
                    (hormigas[n][0], hormigas[n][0]-1))[1]/200,
                    pantalla.get_at((hormigas[n][0]+1, hormigas[n][0]-1))[1]/200])
	#Actualizacion de la ventana
	pygame.display.flip()
	pantalla.fill((120, 200, 80))


	
