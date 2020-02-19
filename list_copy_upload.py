#This program will store the items 'apple', 'pear', 'plums',and 'strawberry'
#To a list named my_fruits. Next the list will be copied, and two duplicate lists will be printed out.
#One list will have the name my_fruits and the second name will have the name friends_fruits. 
#Also, two entries will be added to the second list 'friends_fruits' 'peach', and 'nectarine' and the new list with the new items will be disclosed.
#Finally the program will disclose the information in both lists while showing the number of items in each list.
#***storing information in list***
my_fruits = ['apple','pear','plums','strawberry']
#Copying list.
friends_fruits = my_fruits[:]
#Disclosing contents of list my_fruits
print(my_fruits)
#Disclosing contents of list friends_fruits
print(friends_fruits)
#Adding food 'peach' to list friends_fruits
friends_fruits.append('peach')
#Adding 'necatine' to list friends_fruits
friends_fruits.append('nectarine')
#Disclosing list contents of friends_fruits verifying the implementation of new entries were successful.
print(friends_fruits,"\n")
for my_fruit in my_fruits:
	print(f"{my_fruit.title()}.")
# Diclosing information of list my_fruits and disclosing number of entries stored in list.
print(f"Your list contains:{len(my_fruits)} fruits.\n")
for friends_fruit in friends_fruits:
	print(friends_fruit)
#Diclosing information of list friends_fruits and disclosing number of entries stored in list.
print(f"\nYour list contains:{len(friends_fruits)} fruits.")