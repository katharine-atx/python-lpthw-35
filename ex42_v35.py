# Version 2.7 to 3.5: super() can be used without arguments
# is-a / has-a: classes and objects

## Animal is-a object
class Animal(object):
	pass #you could play around here
	
## Dog is-a class of Animal
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a class of Animal
class Cat(Animal):
	def __init__(self, name):
		## Cat has-a name
		self.name = name
		
## Person is-a object
class Person(object):
	def __init__(self, name):
		## Person has-a name
		self.name = name
		## Person has-a pet...default "no"
		self.pet = None
		
## Employee is-a class of Person
class Employee(Person):
	def __init__(self, name, salary):
		## Refers back to Person class-object .name expression
		super().__init__(name)
		## Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass #you could play around here

## Salmon is-a class of Fish
class Salmon(Fish):
	pass #you could play around here

##	Halibut is-a class of Fish
class Halibut(Fish):
	pass #you could play around here

## rover is-a object in object-class Dog
## rover has-a name, "Rover"
rover = Dog("Rover")

## fluffy is-a object in object-class Cat
## fluffy has-a name, "Fluffy"
fluffy = Cat("Fluffy")

## mary is-a object in object-class Person
## mary has a name, "Mary"
mary = Person("Mary")

## mary has-a pet, fluffy
## fluffy is-a object in object-class Cat
mary.pet = fluffy

## frank is-a object in object-class Employee
## frank has-a name, "Frank"
## frank has-a salary, 120000
frank = Employee("Frank", 120000)

## frank has-a pet, rover
## rover is-a object in object-class Dog
frank.pet = rover

## flipper is-a object in object-class Fish
flipper = Fish()

## george is-a object in class Salmon
george = Salmon()

## harry is-a object in class Halibut
harry = Halibut()






