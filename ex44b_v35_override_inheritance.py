# Version 2.7 to 3.5: print()

# Explicit override example:
# Overriding a function in the parent for the child function

class Parent(object):
	def override(self):
		print("PARENT override()")

class Child(Parent):
	def override(self):
		print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()