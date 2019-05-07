#Librerias
import sys, pygame, os

#Variables
ratio = width, height = 800, 500 
blanco = 255,255,255
negro = 0,0,0
fase_dejuego = 0
archivo = str(os.getcwd())

#Clases
pygame.init()
pantalla = pygame.display.set_mode(ratio)


#Imagenes y Sprites
def cargar(imagen):
	return pygame.image.load(archivo+"\Sprites\\"+imagen)
def dibujar(imagen,x,y):
	pantalla.blit(imagen,(x,y))
def dibujar_rectangulo(color,x,y,largo,ancho):
	pygame.draw.rect(pantalla, color, (x,y,largo,ancho))

#Funcion del juego
def juego(): 
	hola = 1

#Funcion de sprites
def renderizacion():
	
	pygame.display.flip() #Actualiza la pantalla

#Ordenes de entrada
Icono = cargar("icono.png")
Logo = cargar("logo.png")
pygame.display.set_caption("Hormiguero")
pygame.display.set_icon(Icono)
pantalla.fill(blanco)

#Bucle principal
while 1:  

#Evento de salida del bucle
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: sys.exit() 
			
#Funciones principales
	juego()
	renderizacion()
	 
