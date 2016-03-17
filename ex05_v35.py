#Python 2.7 to 3.5: the % string format syntax is still supported but will be phased out.
#New method: 'My name is {} and I have {} pets'.format(variable0,variable1)
#-or- format it for understandability to refer to ID variables:
#'My name is {name} & I have {n} pets.'.format(name=name,n=num_pets)

my_name = 'Your Name'
my_age = 27 # not a lie
my_height = 65.0 # inches
my_weight = 160 # lbs
my_eyes = 'green'
my_teeth = 'white'
my_hair = 'brown'

print ("Let's talk about %s." % my_name)
print ("They're %d inches tall." % my_height)
print ("They're %d pounds heavy." % my_weight)
print ("Actually, that's not too heavy.")
print ("They've got %s eyes and %s hair." % (my_eyes, my_hair))
print ("Their teeth are usually %s depending on the coffee. And again, %d isn't bad." % (my_teeth, my_weight))

#here's a tricky one...
print ("If I added my age (%d), my weight (%d) and my height (%d), I get %d." % (my_age , my_weight , my_height , my_age + my_height + my_weight))

