# Version 2.7 to 3.5: print(), input() instead of raw_input()

# Choose your own adventure: the icecream truck cometh
# Using a random integers, random.randint(), for probability element
# Adding time delays with time.sleep() for smoother flow
# Limiting iterations for return to start scenarios with function.counter()

from sys import exit
import time

def icecream():
	time.sleep(6)
	print("Victory! Oh, they have the one you like.")
	time.sleep(5)
	print("Good job, Champ.")
	exit(0)

def abandoned():
	time.sleep(8)
	print("So, it's not stopping...")
	time.sleep(5)
	print("You take your sweaty self back inside...")
	time.sleep(5)
	print("Again...")
	window_peek()
	
def truck_stop():
	import random
	chance = random.randint(1,3)
	if chance == 1:
		icecream()
	else:
		abandoned()

def lazy():
	time.sleep(1)
	print("Yes, take your well earned rest.")
	time.sleep(3)
	print("Again...")
	window_peek()
	
def runner():
	time.sleep(2)
	print("You're gunning for it, running like a demon, yelling,",
	"'Wait! Wait for me, wait!'")
	truck_stop()

def hungry():
	time.sleep(1)
	print("Are you ready to run?\n 1. Yes, ma'am! \n 2. Nope")
	choice = input("> ")
	if choice == "1":
		runner()
	elif choice == "2":
		lazy()
	else:
		print("Huh? I don't have time for this.")
		exit(0)

def caller():
	time.sleep(2)
	print("Good job! You've done your civic duty.")
	exit(0)

def passive():
	time.sleep(1)
	print("Yep, that's a reasonable attitude.")
	time.sleep(3)
	print("Again...")
	window_peek()
	
def cranky():
	time.sleep(1)
	print("Call in a noise complaint for that tune it's blasting?\n",
	"1. Yep\n 2. No, it will be over soon.")
	choice = input("> ")
	if choice == "1":
		caller()
	elif choice == "2":
		passive()
	else:
		print("Huh? I don't have time for this.")
		exit(0)

def sentiment():
	print("Are you feeling...?\n 1. Excited! \n 2. Annoyed")
	choice = input("> ")
	if choice == "1":
		hungry()
	elif choice == "2":
		cranky()
	else:
		print("Huh? I don't have time for this.")
		exit(0)
	
def its_back():
	print("Wait, what!? The truck's looping back around the block!")
	time.sleep(3)
	sentiment()

def first_sighting():
	print("You spot the icecream truck, approaching from the north.")
	time.sleep(3)
	sentiment()
	
def window_peek():
	window_peek.counter += 1
	print("Staring out the window...")
	time.sleep(2)
	if window_peek.counter < 2:
		first_sighting()
	elif window_peek.counter < 5:
		its_back()
	else:
		print("No, time for you to get back to work!")
		exit()

window_peek.counter = 0
window_peek()



