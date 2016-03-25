# Version 2.7 to 3.5: print() and {}/.format(). Also, use int()
# to retain integer class output when dividing.
# Second method example for formatting can be done with the % method but not {}/.format().
# .format() expects a tuple argument, not a function.
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("----------------")
print(poem)
print("----------------")

five = 10 - 2 + 3 - 6
print("This should be five: {}" .format(five))

def secret_formula(started):
	jelly_beans = started * 500
	jars = int(jelly_beans / 1000)
	crates = int(jars / 100)
	return jelly_beans, jars, crates

	
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}" .format(start_point))
print("We'd have {} beans, {} jars, and {} crates." .format(beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
# % formatting with this method:
formatter = "We'd have %d beans, %d jars, and %d crates." 
print(formatter % (secret_formula(start_point)))

