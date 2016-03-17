print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % 'snow') #Note: % syntax for string formatting is being phased out
print ("And everywhere that Mary went.")
print ("." * 10) #What? What did that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#Version 2.7 to 3.5: print() encloses the expression to be printed.
print (end1 + end2 + end3 + end4 + end5 + end6) #a comma here won't pull the second print() item onto the same line.
print (end7 + end8 + end9 + end10 + end11 + end12)

#To pull the second expression printed onto the same line, do not close the ().
print (end1 + end2 + end3 + end4 + end5 + end6, #put a comma here. a space " " is added.
end7 + end8 + end9 + end10 + end11 + end12)