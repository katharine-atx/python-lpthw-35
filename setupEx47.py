# Version 2.7 to 3.5: Note .pyc to .cpython-35 
# extension for compiled python file

# Prior to running script:
# Copy skeleton (from Ex 46) to ex47.
# Replace NAME with ex47 for names and file content.
# Remove any compiled python files.

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
	'packages': ['ex47'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)

