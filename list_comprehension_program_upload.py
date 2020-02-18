# This program will store the numbers ranging from 1-50 in a list and then raise each number to the 4th power. 
# Next, it will print out each value in the list followed by the  min max and sum values 
list_of_numbers_from_one_to_50 = [value**4 for value in range(1,51)]
print(list_of_numbers_from_one_to_50)
#print min and max value in the list
print("The minimum value in this list is:",min(list_of_numbers_from_one_to_50))
print("The maximum value im this list is:",max(list_of_numbers_from_one_to_50))
print("The sum of the values in this list is:",sum(list_of_numbers_from_one_to_50))
