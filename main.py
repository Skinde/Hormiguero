#Librerias
import sys, pygame, os

#Variables
ratio = width, height = 800, 500 
fondo = 255,255,255
game_phase = 0
#Clases
pygame.init()
pantalla = pygame.display.set_mode(ratio)
archivo = str(os.getcwd())

#Imagenes y Sprites
Icono = pygame.image.load(archivo+"\icono.png").convert_alpha()
Logo = pygame.image.load(archivo+"\logo.png").convert_alpha()
#Funcion del juego
def juego(): 
	hola = 1

#Funcion de sprites
def renderizacion():
	pantalla.blit(Logo,Logo.get_rect())
	pygame.display.flip()

#Ordenes de entrada
pygame.display.set_caption("Hormiguero")
pygame.display.set_icon(Icono)
pantalla.fill(fondo)

#Bucle principal
while 1:  

#Evento de salida del bucle
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: sys.exit() 
			
#Funciones principales
	juego()
	renderizacion()
	 
