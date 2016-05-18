# Version 2.7 to 3.5: print()

# Run order dependent override example:
# alter the behavior before or after the Parent class’s version runs

class Parent(object):
	def altered(self):
		print("PARENT altered()")
		
class Child(Parent):

	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		# Parent function "super"cedes child
		super(Child, self).altered() 
		print("CHILD, AFTER PARENT altered()")
		
dad = Parent()
son = Child()

dad.altered()
son.altered()
	