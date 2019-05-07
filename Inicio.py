Utec = cargar("utec.png")
Icono = cargar("icono.png")
Logo = cargar("logo.png")
pygame.display.set_caption("Hormiguero")
pygame.display.set_icon(Icono)
pantalla.fill(blanco)
hormiga_reina = cargar("hormiga_reina.png")
for n in range(450):
	for x in range(800):
		mapa[n][x] = 1
