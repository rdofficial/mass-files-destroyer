"""
rewriter.py - Mass Files Destroyer

Created by : Rishav Das (https://github.com/rdofficial/)
Created on : September 16, 2021

Last modified by : -
Last modified on : -
"""

# Importing the required functions and modules
from os import path, rename, listdir
from base64 import b64encode, b64decode
from sys import platform

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

def main():
	# Asking the user to specify the directory location
	directory = input(blue + 'Enter the directory location : ' + yellow)
	print(defcol, end = '')

	# Calling the rewriter function in order to start the task
	rewriter()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses the CTRL+C key combo, then we exit the script

		exit()
	except Exception as e:
		# If there are any errors encountered during the process, then we continue to display the error message on the console screen and then exit

		print(red_rev + f'[ Error : {e} ]' + defcol)