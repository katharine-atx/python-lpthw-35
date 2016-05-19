# Version 2.7 to 3.5: print()

# Composition used to same effect as the inheritane example (ex44d)...

class Other(object):
	def override(self):
		print("OTHER override")
	def implicit(self):
		print("OTHER implicit()")
	def altered(self):
		print("OTHER altered()")
		
class Child(object):
	def __init__(self):
		self.other = Other()
	def implicit(self):
		self.other.implicit()
	def override(self):
		print("CHILD override()")
	def altered(self):
		print("CHILD, BEFORE OTHER altered()")
		self.other.altered()
		print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()