# While loops...
# Version 2.7 to 3.5: print() and use {}/.format 

i = 0
numbers = []

while i < 6:
	print("At the top i is {}" .format(i))
	numbers.append(i)
	
	i = i + 1
	print("Numbers now: ", numbers)
	print("At the bottom i is {}" .format(i))
	
print("The numbers: ")

for num in numbers:
	print(num)
	