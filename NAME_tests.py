# Version 2.7 to 3.5: print()
# Creating a skeleton file...

# Works with setup.py

from nose.tools import *
import NAME

def setup():
	print("SETUP!")
	
def teardown():
	print("TEAR DOWN!")
	
def test_basic():
	print("I RAN!")
	
