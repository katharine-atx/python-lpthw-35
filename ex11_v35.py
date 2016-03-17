#Python 2.7 to 3.5: Use input() rather than raw_input() and switch to {} .format from % format string
#getting input from a user

print ("How old are you?",)
age = input()
print ("How tall are you?",)
height = input()
print ("How much do you weigh?",)
weight = input()

print ("So, you're {} old, {} tall and {} heavy." .format(
	age, height, weight))