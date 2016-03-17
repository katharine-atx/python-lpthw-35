#The Python 2.7 way - which still works with 3.5:
Side_bar = '''
\t "There is this explanation 
that goes onto multiple lines.
One of the best quotes ever
according to many."
\t\t - %s
'''
print (Side_bar % "Someone")

#The Python 3.5 way:
author = "Someone"

Side_bar2 = '''
\t "There is this explanation 
that goes onto multiple lines.
One of the best quotes ever
according to many."
\t\t - {}
'''.format(author)

print (Side_bar2)