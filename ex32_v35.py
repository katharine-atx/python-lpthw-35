# Loops and lists...
# Version 2.7 to 3.5: print(), use {}/.format rather than % formatter
# Note on new formatter: '' single quotes will not be printed by 
# default for string elements.

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# for loop going through a list...
for number in the_count:
	print("This is the count {}" .format(number))

for fruit in fruits:
	print("A fruit of type: {}" .format(fruit))

for i in change:
	print("I got {}" .format(i))

# building lists, starting with an empty one...

elements = []

# then use the range function to 0 to 5 counts
for i in range(0, 6):
	print("Adding {} to the list." .format(i))
	#append is a function for lists...
	elements.append(i)

# printing out elements as a loop...
for i in elements:
	print("Element was: {}" .format(i))
	
