import random 
#Semilla aleatoria
random.seed(datetime.now())
#Cargado de imagenes
Utec = cargar("utec.png")
Icono = cargar("icono.png")
Logo = cargar("logo.png")
hormiga_reina = cargar("hormiga_reina.png")

#Edicion de ventana (titulo,icono)
pygame.display.set_caption("Hormiguero")
pygame.display.set_icon(Icono)
pantalla.fill(blanco)


if fase_dejuego == 0:
		dibujar(Utec, 285, 140)
		pygame.display.flip()
		time.sleep(2)

#Informacion de todas las hormigas
probabilidad = []
hormigas = []
verdosidad = []
rojosidad = []
calculadora = []
#Comida
comida = []

for _ in range(100):
	comida.append([(random.randint(0,1000)), (random.randint(0,1000))])

for r in range(20):
	hormigas.append([400+r,250+r])

