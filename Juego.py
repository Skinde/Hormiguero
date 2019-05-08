import main, random
random.seed(12312836)

def juego(): 
	if fase_dejuego == 0:
		global hormigax 
		global hormigay 
		hormigax = 100
		hormigay = 45
	movex = random.randint(0, 2)
	movey = random.randint(0, 2)
	if movex == 0:
		hormigax -= 5
	if movex == 2:
		hormigax += 5
	if movey == 0 and hormigay > 45:
		hormigay -= 5
	if movey == 2:
		hormigay += 5





