# Version 2.7 to 3.5: No changes.
# Automated testing example...

class Room(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		
	def go(self, direction):
		return self.paths.get(direction, None)
	
	def add_paths(self, paths):
		self.paths.update(paths)