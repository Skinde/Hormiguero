#Librerias
import sys, pygame, os, time, importlib

#Variables
ratio = width, height = 800, 500 
blanco = 255,255,255
negro = 0,0,0
fase_dejuego = 0
archivo = str(os.getcwd())
mapa = [[0 for x in range(800)] for y in range(450)]
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
