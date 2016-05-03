# This exercise is meant to help you quiz yourself on object-oriented phrases in python.
# Run note: default run outputs object-oriented phrases from PHRASES dict first, followed by English.
# Run as ex41_v35.py english to get the inverse order (English-language translations first).

# Version 2.7 to 3.5: Several types of changes required...
# Basic syntax: print(), input() instead of raw_input(), 
# 	{}/.format() instead of % formatter.
# Library note: use urllib.request as library for urlopen
# Changes to default classes: dict key and urlopen()
#	In version 3, dict.keys() output is set-like and you can't call objects by index as desired
# 	in the Try/While True section of this exercise. Instead use a list() for the key. More in:
# http://stackoverflow.com/questions/18552001/accessing-dict-keys-element-by-index-in-python3
# 	Loading the WORDS requires decoding from ASCII so you get string, not bytes. More in:
# http://stackoverflow.com/questions/16699362/python3-error-typeerror-cant-convert-bytes-object-to-str-implicitly


import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# PHRASES dict...
PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
		"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'"
}

# Drilling phrases first...
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
	
# Loading the words from the URL...
for word in urlopen(WORD_URL):
	WORDS.append(word.strip().decode('ascii'))

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
		random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		
	for sentence in snippet, phrase:
		result = sentence[:]
		
		# fake class names...
		for word in class_names:
			result = result.replace("%%%", word, 1)
			
		# fake other names...
		for word in other_names:
			result = result.replace("***", word, 1)
		
		# fake parameter lists...
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
		
	return results
	
# Adding break option with input() == "exit"...
print("\n******Type exit for break, ENTER to continue******\n")
try:
	while True:
		snippets = list(PHRASES)
		random.shuffle(snippets)
		
		if input() == "exit":
			break
			
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
			
			print(question)
			
			input("> ")
			print("ANSWER: {}\n\n" .format(answer))
		
except EOFError:
	print("\nBye")		