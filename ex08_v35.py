#Version 2.7 to 3.5: Only change here is print to print()
#But not that % syntax for string formatting is being phased out

#ok, a format for text...
formatter = "%r %r %r %r"
#So basically 4 components plug and play with spaces in between
# print it using variable % (values) 
print (formatter % (1,2,3,4))
print (formatter % ("one", "two", "three", "four"))
#So yes, ^it can do either value type
#But what about True/False values?...
print (formatter % (True, False, False, True))
#Or nesting it inside itself?
print (formatter % (formatter, formatter, formatter, formatter))
#Look how it's no issue to carry on an expression on multiple lines with commas.
print (formatter % (
"I had this thing...",
"that you could type up right.",
"But it didn't sing,",
"so I said goodnight."
))
