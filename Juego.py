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


def juego(): 
	hola = 1
