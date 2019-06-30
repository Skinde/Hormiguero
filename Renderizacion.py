def movimiento(hormigas):
    espacios={"ul":0,"u":0,"ur":0,"l":0,"r":0,"dl":0,"d":0,"dr":0}
    for i in espacios:
        espacios[i]=probabilidad

def probabilidad(x,y):
    (hormonas*verdosidad)
    for i in range(8):
        sumatoria=sumatoria+probabilidad()

def renderizacion():  # PONGAN SU CODIGO AQUI ESTO SE EJECUTA EN UN BUCLE
	#Dibujo de la hormiga 
	for d in range(len(hormigas)):
		dibujar_rectangulo(negro, hormigas[d][0], hormigas[d][1], 4, 4)
	del verdosidad[:]
	del rojosidad[:]
	for n in range(20):
		print(hormigas[n][0], hormigas[n][0])
		verdosidad.append([pantalla.get_at((hormigas[n][0]-1, hormigas[n][0]+1))[1]/200, pantalla.get_at((hormigas[n][0], hormigas[n][0]+1))[1]/200, pantalla.get_at((hormigas[n][0]+1, hormigas[n][0]+1))[1]/200, pantalla.get_at((hormigas[n][0]-1, hormigas[n][0]))
                        [1]/200, pantalla.get_at((hormigas[n][0]+1, hormigas[n][0]))[1]/200, pantalla.get_at((hormigas[n][0]-1, hormigas[n][0]-1))[1]/200, pantalla.get_at((hormigas[n][0], hormigas[n][0]-1))[1]/200, pantalla.get_at((hormigas[n][0]+1, hormigas[n][0]-1))[1]/200])
		rojosidad.append([pantalla.get_at((hormigas[n][0]-1, hormigas[n][0]+1))[0]/200, pantalla.get_at((hormigas[n][0], hormigas[n][0]+1))[0]/200, pantalla.get_at((hormigas[n][0]+1, hormigas[n][0]+1))[0]/200, pantalla.get_at((hormigas[n][0]-1, hormigas[n][0]))
                        [0]/200, pantalla.get_at((hormigas[n][0]+1, hormigas[n][0]))[0]/200, pantalla.get_at((hormigas[n][0]-1, hormigas[n][0]-1))[0]/200, pantalla.get_at((hormigas[n][0], hormigas[n][0]-1))[0]/200, pantalla.get_at((hormigas[n][0]+1, hormigas[n][0]-1))[0]/200])
	#Dibujo de comida
	for c in range(len(comida)):
		dibujar_rectangulo((200,0,0), comida[c][0], comida[c][1], 3, 3)
	
	#Actualizacion de la ventana
	pygame.display.flip()
	pantalla.fill((120, 200, 80))


