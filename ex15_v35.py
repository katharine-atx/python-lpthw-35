#Python 2.7 to 3.5: use input() instead of raw_input()

from sys import argv
script, filename = argv
#first 2 lines are importing filename as an argument in your code

txt = open(filename)

print ("Here's your file {}" .format(filename))
print (txt.read())

print ("Type the file name again: ")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())

