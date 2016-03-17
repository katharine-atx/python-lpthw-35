# Re-writing the prompts for form input
# Python 2.7 to 3.5: Use input(), not raw_input() and {} + .format() for format string

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print ("So, you're {} old, {} tall and {} heavy." .format(
	age, height, weight))
	