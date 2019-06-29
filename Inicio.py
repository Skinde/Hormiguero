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
