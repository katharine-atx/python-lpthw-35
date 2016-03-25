#Version 2.7 to 3.5: Changes include print() and {}/.format() instead of %.
#Also, output in 3.5 will default to numeric class for division.
#Use int() to retain integer class output.

def add(a,b):
	print("ADDING {} + {}" .format(a, b))
	return a + b 

def subtract(a,b):
		print("SUBTRACTING {} - {}" .format(a,b))
		return a - b 

def multiply(a,b):
	print("MULTIPLYING {} * {}" .format(a,b))
	return a * b 

def divide(a,b):
	print("DIVIDING {} / {}" .format(a,b))
	return int(a / b)

print ("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age: {}, Height: {}, Weight: {}, IQ: {}" .format(age, height, weight, iq))

# A puzzle for the extra credit ....
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")

#Challenge: a simple formula for what:

simple_what = age + height - (weight * int(iq / 2))

print("With a simplified function: {}" .format(simple_what))

