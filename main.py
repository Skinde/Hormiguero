#Librerias
import sys, pygame, os, time

#Variables
ratio = width, height = 800, 500 
blanco = 255,255,255
negro = 0,0,0
fase_dejuego = 0
archivo = str(os.getcwd())
mapa[800][450]
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
	if fase_dejuego == 0:
		dibujar(Utec, 285, 140)
		pygame.display.flip()
		time.sleep(2)
		pantalla.fill(blanco)
	pygame.display.flip() #Actualiza la pantalla

#Ordenes de entrada
Utec = cargar("utec.png")
Icono = cargar("icono.png")
Logo = cargar("logo.png")
pygame.display.set_caption("Hormiguero")
pygame.display.set_icon(Icono)
pantalla.fill(blanco)

for n in range(450):
	for x in range(800):
		mapa[n][x] = "Tierra"


#Bucle principal
while 1:  

#Evento de salida del bucle
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: sys.exit() 
			
#Funciones principales
	juego()
	renderizacion()
	if fase_dejuego == 0:
		fase_dejuego = 1
	 
