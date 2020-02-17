#This program will print out the list contents that are stored in the variable 'animals' with an attached message. Next, the program will end the loop with the following statement ' All of the pets posses the ability to fly!'
animals = ['bird','bat','flie']
for animal in animals:
	print(f"A {animal.title()} would make a gret pet.\n")
print("All of these pets posses the ability to fly!")
