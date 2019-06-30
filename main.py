#Librerias
import sys, pygame, os, time, importlib, random
from datetime import datetime

#Variables
ratio = width, height = 800, 500 
blanco = 255,255,255
negro = 0,0,0
fase_dejuego = 0
archivo = str(os.getcwd())
mapa = [[0 for x in range(800)] for y in range(500)]
global hormigax
global hormigay
#Clases
pygame.init()
pantalla = pygame.display.set_mode(ratio)


#Funciones Personales
def cargar(imagen):
	return pygame.image.load(archivo+"\Sprites\\"+imagen)
def dibujar(imagen,x,y):
	pantalla.blit(imagen,(x,y))
def dibujar_rectangulo(color,x,y,largo,ancho):
	pygame.draw.rect(pantalla, color, (x,y,largo,ancho))




#Funcion del juego
exec(open(archivo+"\Juego.py").read())
#Funcion de sprites
exec(open(archivo+"\Renderizacion.py").read())
#Ordenes de entrada
exec(open(archivo+"\Inicio.py").read())


#Bucle principal
while 1:  
#Evento de salida del bucle
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
	
#Funciones principales
	juego()
	renderizacion()
	if fase_dejuego < 3:
		fase_dejuego += 1
	
	 
