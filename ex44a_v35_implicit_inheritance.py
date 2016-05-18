# Version 2.7 to 3.5: print()

# Implicit inheritance example:
# Defining a function in the parent, but not in the child

class Parent(object):
	def implicit(self):
		print("PARENT implicit()")
		
class Child(Parent):
	pass #indicates there is nothing new to define this class
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()