# Version 2.7 to 3.5: No changes.
#Creating a skeleton project directory...

# Edit this file so that it has your contact information 
# and is ready to go for when you copy it.

# Works with NAME_tests.py

# Package requirements: pip, distribute, nose, virtualenv(optional)
# Prior to running script, create the appropriate directories for the project...
#$ mkdir projects
#$ cd projects
#$ mkdir skeleton
#$ cd skeleton
#$ mkdir NAME
#$ mkdir tests
#$ mkdir bin
#$ mkdir docs
# -- In Windows, creating script items --
#$ new-item -type file NAME/__init__.py
#$ new-item -type file tests/__init__.py

# To test this script, from skeleton dir, run command: nosetests
# Should run 1 test.

# To reuse this skeleton for a new project:
	# 1. Copy and rename skeleton directory.
	# 2. Rename and move the NAME directory to project name.
	# 3. Edit setup.py.
	# 4. Rename tests/NAME_tests.py to your project name.
	# 5. Test (nosetest)

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My Project',
	'authr': 'My Name',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)

