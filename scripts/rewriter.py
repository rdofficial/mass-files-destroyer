"""
rewriter.py - Mass Files Destroyer

Created by : Rishav Das (https://github.com/rdofficial/)
Created on : September 16, 2021

Last modified by : Rishav Das(https://github.com/rdofficial/)
Last modified on : September 21, 2021

Changes made in the last modification :
1. Added the code for the rewriter() function.

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
from os import path, listdir, rename, chdir
from base64 import b64encode, b64decode
from sys import platform

# Checking whether color code variables are supported or not
if 'linux' in platform:
	# If the platform type is linux, then we define the color code variables

	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	red_rev = '\033[07;91m'
	defcol = '\033[00m'
else:
	# If the platform type is not linux, then we define the color code variables as blank strings

	red = ''
	green = ''
	yellow = ''
	blue = ''
	red_rev = ''
	defcol = ''

def rewriter(directory):
	""" This function serves the functionality of rewritting the files in the entire directory tree as per specified by the user. The function uses the base64 module functions b64 encode in order to create some waste and unreadable terms for the files to make them unreadable. The files destroyed using this function can never be retrieved back to its original and readable state. The function is a recursive function, when it is provided with directories with its own sub-directories, then the function re-calls itself again and more inner sub-folder files are destroyed there after. The function takes only one sort of parameter : directory. This parameter stores the target directory location specified by the user. """

	# Changing the current working directory to the user specified directory
	chdir(directory)

	for file in listdir():
		# Iterating through each file in the directory

		if path.isfile(file):
			# If the current iteration is a file, then we continue to re-write it

			# Reading the contents of the file
			contents = open(file, 'rb').read()

			# Destroying and re-writting the contents of the file
			contents = b64encode(contents).decode()
			contents = contents[::-1]
			contents = contents[0:len(contents)/2]

			# Saving the contents back to the file
			open(file, 'w').write(contents)

			# Destroying the filename
			newname = b64encode(file.encode()).decode()

			# Renaming the file with the new name
			rename(file, newname)
		elif path.isdir(file):
			# If the current iteration is a directory, then we re-call the rewriter() function by passing the next directory root

			directory = path.join(directory, file)
			rewriter(directory)
		else:
			# If the current iteration is neither a file nor a directory, then we raise a fucking error with a custom message

			raise TypeError(f'{file} is neither recognized as a file, nor recognized as a folder.')

def main():
	# Asking the user for the directory location
	directory = input(blue + 'Enter the directory location : ' + yellow)
	print(defcol, end = '')

	# Calling the rewriter() function
	rewriter(directory)

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		# If the user presses CTRL+C key combo, then we exit the script

		exit()
	except Exception as e:
		# If there are any errors encountered during the process, then we display the error message on the console screen

		print(red_rev + f'[ Error : {e} ]' + defcol)
		exit()