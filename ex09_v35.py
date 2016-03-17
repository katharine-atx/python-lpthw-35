days = "Mon Tue Wed Thu Fri Sat Sun"
#\n new line breaks for month list
months = """Jan\nFeb\nMar\nApr\nMay\nJun\nJul
\nAug\nSep\nOct\nNov\nDec"""
#Python 2.7 to 3.5: Use """ not an EOL comma if you want a string definition across multiple lines of code.

print ("Here are the days:", days)
print ("Here are the months:", months)

print ("""
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6...
""")