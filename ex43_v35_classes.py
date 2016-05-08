# Version 2.7 to 3.5: 

# Context:
# This exercise is a mapped out definition for 
# a choose-your own adventure type game with a 
# sci-fi theme...

class Scene(object):
	def enter(self):
		pass # add content here
		
class Engine(object):
	def __init__(self, scene_map):
		pass # add content here
	def play(self):
		pass #...
		
class Death(Scene):
	def enter(self):
		pass #...
		
class CentralCorridor(Scene):
	def enter(self):
		pass #...
		
class LaserWeaponArmory(Scene):
	def enter(self):
		pass #...
		
class TheBridge(Scene):
	def enter(self):
		pass #...
		
class EscapePod(Scene):
	def enter(self):
		pass #...
		
class Map(object):
	def __init__(self, start_scene):
		pass #...
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
