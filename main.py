#Librerias
import sys, pygame

#Variables
ratio = width, height = 800, 500 
fondo = 255,255,255

#Clases
pygame.init()
pantalla = pygame.display.set_mode(ratio) 

#Funcion del juego
def juego(): 
	hola = 1

#Funcion de sprites
def renderizacion(): 
	pygame.display.flip()


pantalla.fill(fondo)

#Bucle principal
while 1:  

#Evento de salida del bucle
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: sys.exit() 
			
#Funciones principales
	juego()
	renderizacion()
	 
