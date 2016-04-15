# Version 2.7 to 3.5: print(), use {}/.format() instead of % foramtters.
# dicts (dictionaries) continued...

# Testing the hashmap dictionary module to recreate Ex 39 output...

import hashmap #import module

# recreate mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a mapping of states to city within
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some additional cities to the dict
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print a few cities...
print('-' * 10)
print("NY State has: {}" .format(hashmap.get(cities, 'NY')))
print("OR State has: {}" .format(hashmap.get(cities, 'OR')))

# print a few states...
print('-' * 10)
print("Michigan's abbreviation is: {}" .format(hashmap.get(states,'Michigan')))
print("Florida's abbreviation is: {}" .format(hashmap.get(states, 'Florida')))

# get the same info using the state then cities dict...
print('-' * 10)
print("Michigan has: {}" .format(hashmap.get(cities, hashmap.get(states, 'Michigan'))))
print("Florida has: {}" .format(hashmap.get(cities, hashmap.get(states, 'Florida'))))

# print all stored state abbreviations
print('-' * 10)
hashmap.list(states)

# print every stored city
print('-' * 10)
hashmap.list(cities)

print('-' * 10)
state = hashmap.get(states, 'Texas')

if not state:
	print("Sorry, no Texas.")
	
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print("The city for the state 'TX' is {}" .format(city))
# default values using ||= with the nil result
# can you combine the above on one line?


