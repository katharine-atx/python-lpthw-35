# Python 2.7 tp 2.5: Print()
# adding an argument (script object?) into the script
# the import line:
from sys import argv 
# defining argv
script, first, second, third = argv #These will need to be supplied when running
# here's a print just to check what you've done
print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

#Alternately, combine:
first = input("What's the first field? " )
second = input("What's the second field? " )
third = input("What's the third field? " )

print("Here are your 3 fields: {}, {}, {}.".format(first,second,third))