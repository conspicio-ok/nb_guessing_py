from random import randint as rand

def search_nb(nb) :
	laps = 10
	nb_usr = -1
	res = False
	while (nb_usr != nb and laps) :
		laps -= 1
		nb_usr = int(input("\nGive a number between 0 and 100\n"))
		if (nb_usr > nb) :
			print("It's minus")
		elif (nb_usr < nb) :
			print("It's more")
	if (nb == nb_usr) :
		res = True
	return res

if __name__ == "__main__" :
	nb = rand(0, 100)
	if (search_nb(nb)):
		print("You find the number !")
	else :
		print("Try again ;)")
