# Version 2.7 to 3.5: print()
# dicts (dictionaries), modules and classes
# Note on dict v list. A dict does not preserve order.

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# Alternatively, import the mystuff module...
import mystuff
mystuff.apple()

# Or define a function...
def apple():
	print("I AM APPLES!")
	
# Now access that new variable via the mystuff module...
import mystuff

mystuff.apple()
print(mystuff.tangerine)

# Rather than a module, you might create a class
  # Why use a class? It's self contained so one class won't interfere 
  # with another within the program. Modules on the other hand 
  # generally apply for the entire program once imported.

# Here's a class example...
class MyStuff(object):
	
	def __init__(self):
		self.tangerine = "And now a thousand years between"
	
	def apple(self):
		print("I AM CLASSY APPLES!")

# Instantiating (creating) a class "copy" by calling like a function
thing = MyStuff()
thing.apple()
print(thing.tangerine)

# To review: getting objects from containers

	# dict style
mystuff = {'apple': "I AM APPLES!"} # re-defining since module over-wrote
mystuff['apple']

	# module style
import mystuff # this is why its best not to name objects/functions the same...
mystuff.apple()
print(mystuff.tangerine)

	# class style
thing = MyStuff() # wisely named differently...
thing.apple()
print(thing.tangerine)




