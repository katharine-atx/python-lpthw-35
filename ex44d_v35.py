# Version 2.7 to 3.5: print()

# Combined example of implicit inheritance, override and 
# run-order dependent alterations.

class Parent(object):
	def override(self):
		print("PARENT override()")
	def implicit(self):
		print("PARENT implicit()")
	def altered(self):
		print("PARENT altered()")
	
class Child(Parent):
		def override(self):
			print("CHILD override()")
		def altered(self):
			print("CHILD, BEFORE PARENT altered()")
			# Parent "super"ceding Child...
			super(Child, self).altered()
			print("CHILD, AFTER PARENT altered()")
			
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
