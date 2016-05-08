# Version 2.7 to 3.5: print(), input() v. raw_input(), use {}/.format()
# rather than % formatters.

from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print("This scene is not yet configured. Subclass",
		"it and implement enter().")
		exit(1)
		
class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
	
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		# printing out the last scene...
		current_scene.enter()
		
class Death(Scene):

	quips = [
		#Add list of witty taunts here....
	]
		
def enter(self):
	print(Death.quips[randint(0, len(self.quips)-1)])
	exit(1)
	
class CentralCorridor(Scene):

	def enter(self):
		# Add scene narrative via print()...
		print("Story point with action options....",
		"shoot!, dodge!, tell a joke")
		
		action = input("What do you do?\n\n")
	
		if action == "shoot!"
			# Add scene narrative via print()...
			print("Story point, resulting in player death...")
			return 'death'
			
		elif action == "dodge!"
			# Add scene narrative via print()...
			print("Story point, sadly also ending in death.")
			return 'death'
			
		elif action == "tell a joke"
			# Add scene narrative via print()...
			print("Story point, this works, actually.")
			return 'laser_weapon_armory'
			
		else:
			print("DOES NOT COMPUTE!")
			return 'central_corridor'
			
class LaserWeaponArmory(Scene):

	def enter(self):
		# Add scene narrative via print()...
		print("Bottom line, you need to guess a 3-digit code.")
		code = "{}{}{}" .format(randint(1,9))
		guess = input("[keypad]> ")
		
	if guess == code:
		# Add scene narrative via print()...
		print("How often would someone actually guess the",
		"correct code? Is so, go on to the bridge.")
		return 'the_bridge'
	else:
		# Add scene narrative via print()...
		print("So you die in this case. Not a lot of winners here.")
		return 'death'
			
class TheBridge(Scene):
	
	def enter(self):
	# Add scene narrative via print()...
	print("So, you're not the only one on the bridge. Do you",
	"....throw the bomb OR slowly place the bomb?")
	
	action = input("> ")
	
	if action == "throw the bomb":
		# Add scene narrative via print()...
		print("It backfires. You die in this one.")
		return 'death'
		
	elif action == "slowly place the bomb":
		# Add scene narrative via print()...
		print("Not too surprising this is the less deadly choice",
		"Now to the escape pod!")
		return 'escape pod'
	else:
		print("DOES NOT COMPUTE!")
		return the_bridge
		
	class EscapePod(Scene):
	
		def enter(self):
			# Add scene narrative via print()...
			print("Time to guess again.... Which pod # do you take?",
			"There are 5 here.")
			good_pod = randint(1,5)
			guess = input("[pod #]> ")
			
			if int(guess) != good_pod:
				#Add scene narrative via print()...
				print("You jump into pod {} and hit EJECT." .format(guess))
				print("You die in this one however...")
				return 'death'
				
			else:
				#Add scene narrative via print()...
				print("You jump into pod {} and hit EJECT." .format(guess))
				return 'finished'
				
		class Finished(Scene):
			def enter(self):
				print("Amazing! You win!!!")
				return 'finished'
				
		class Map(object):
		
			scenes = {
				'central_corridor': CentralCorridor(),
				'laser_weapon_armory': LaserWeaponArmory(),
				'the_bridge': TheBridge(),
				'escape_pod': EscapePod(),
				'death': Death(),
				'finished': Finished(),
			}
			
			def __init__(self, start_scene):
				self.start_scene = start_scene
				
			def next_scene(self, scene_name):
				val = Map.scenes.get(scene_name)
				return val
				
			def opening_scene(self):
				return self.nect_scene(self.start_scene)
				
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
				
		

