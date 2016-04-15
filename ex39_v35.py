# Version 2.7 to 3.5: print()
# dicts (dictionaries)

# Here's a list for comparison...
things = ['a', 'b', 'c', 'd']
print (things[1])
# b
things[1] = 'z'
print(things[1])
# z
things
# ['a', 'z', 'c', 'd']


# And here's a dictionary with non-integer indices...
stuff = {'name': 'Zed', 'age':39, 'height': 6 * 12 + 2}
print(stuff['name'])
# Zed
print(stuff['age'])
# 39
print(stuff['height'])
# 74
stuff['city'] = "San Francisco"
print(stuff['city'])
# San Francisco

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
# Wow
print(stuff[2])
# Neato
stuff
# {'city': 'San Francisco', 2: 'Neato', 'name': 'Zed', 1: 'Wow', 'age': 39, 'height': 74}

# deleting dictionaries...
del stuff['city']
del stuff[1]
del stuff[2]
stuff
# {'name': 'Zed', 'age': 39, 'height': 74}

# A more complex dictionary example...

# create a mapping of state to abbreviation...
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them...
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
	print("{} is abbreviated {}" .format(state, abbrev))
	
# print every city in state
Add here

# now do both at the same time
print('-' * 10)
for state, abbrev in cities.items():
	print("{} state is abbreviated {} and has city {}" .format(
		state, abbrev, cities[abbrev]))

print('-' * 10)

# get an abbreviation by state that might not be there (avoiding error)...
state = states.get('Texas')

if not state:
	print("Sorry, no Texas")
	
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: {}" .format(city))
		
