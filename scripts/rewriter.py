"""
"""

# Importing the required functions and modules
from os import path, rename, listdir
from base64 import b64encode, b64decode

# Defining the color code variables for the colored output
if 'linux' in platform:
	# If the platform is of linux type, then we define the color code variables

	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	red_rev = '\033[07;91m'
	yellow_rev = '\033[07;93m'
	defcol = '\033[00m'
else:
	# If the platform is not of linux type, then we define the variables as empty

	red = ''
	green = ''
	yellow = ''
	blue = ''
	red_rev = ''
	yellow_rev = ''
	defcol = ''

# Defining some global variables required by the script
files = [] 