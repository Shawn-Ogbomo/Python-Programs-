#This program will store various foods inside a list named foods.
#Then it will loop though the foods in the list in search of the entry 'fries'
#Once the entry 'fries' is found, the variable 'message' is capitalized and then printed. 
foods = ['pizza','burgers','fries']
message = "are my favorite food!"
for food in foods:
	if food == 'fries':
		print(food.title(),message)
