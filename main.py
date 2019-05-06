import sys, pygame
pygame.init()

size = width, height = 320, 240 
speed = [2,2]
black = 0, 0, 0

screen = pygame.display.set_mode(size) #Clase ventana

while 1:  #Loop principal 
	for event in pygame.event.get(): #Evento test
		if event.type == pygame.QUIT: sys.exit()
	screen.fill(black)
	pygame.display.flip()
	#hola
	#EFICIENCIAygygy