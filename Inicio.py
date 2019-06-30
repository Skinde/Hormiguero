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

hormigas = []
probmovhor = []

for r in range(20):
	hormigas.append([200+r,200+r])
for n in range(20):
	probmovhor.append([[pantalla.get_at(((hormigas[n][0])-1, (hormigas[n][1])-1))]])
