"""
renamer.py - Mass Files Destroyer

This script serves the functionality of renaming the files listed in the user specified directory. The script uses the encoding changing method in order to rename the files. This script defines two important functions : renamer_destroyer, renamer_restorer. Both of the functions works under the renaming algorithm, but result of both are opposite. The renamer_destroyer() function renames the file from the original format to the base64 format and thus destroying the original name of it. On the other hand, the renamer_restorer() function restores the original name by changing the encoding of the base64 format filename back to the original utf-8 format.

Created by : Rishav Das (https://github.com/rdofficial/)
Created on : September 17, 2021

Last modified by : -
Last modified on : -
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

def renamer_destroyer(directory):
	""" This function serves the functionality of renaming of all the files in the entire directory tree. The renaming of the files occur here in such a way that the original names are replaced by some of the unreadable format names, thus making the files unrecognizable and so-called destroyed. """

	for file in listdir(directory):
		# Iterating through each of the files in the current folder

		if path.isfile(file):
			# If the currently iterated item is a file, then we continue the process

			# Creating the new name of the file (Encoding the original filename to base64 format)
			newname = b64encode(file.encode()).decode()
			
			# Creating the entire paths for the filenames to avoid errors and execute the process fluently
			newname = path.join(directory, file)
			file = path.join(directory, file)

			# Renaming the file with the encoded filename
			rename(file, newname)

			# Printing the message on the console screen
			print(f'[{yellow}!{defcol}] {green}{file}{defcol} -> {red}{newname}{defcol}')
		elif path.isdir(file):
			# If the currently iterated item is a directory, then we recall the function with mentioning this new directory in order to execute the task all over the directory tree

			file = path.join(directory, file)
			renamer_destroyer(file)
		else:
			# If the currently iterated item is neither a file nor a directory, then we display the raise the error with a custom message

			raise TypeError(f'{file} is neither recognized as a file nor as a directory.')

def renamer_restorer(directory):
	""" This function serves the functionality of renaming of all the files whose filenames are destroyed using the renamer_destroyer() function. This function only works with those directory tree where the destroyer function has been already executed, or else an healthy directory tree will get infected using this function's crude operations. """

	for file in listdir(directory):
		# Iterating through each of the files in the current folder

		if path.isfile(file):
			# If the currently iterated item is a file, then we continue the process

			# Creating the new name of the file (Encoding the base64 format name to the original utf-8 format)
			newname = b64decode(file.encode()).decode()
			
			# Creating the entire paths for the filenames to avoid errors and execute the process fluently
			newname = path.join(directory, file)
			file = path.join(directory, file)

			# Renaming the file with the encoded filename
			rename(file, newname)

			# Printing the message on the console screen
			print(f'[{yellow}!{defcol}] {red}{file}{defcol} -> {green}{newname}{defcol}')
		elif path.isdir(file):
			# If the currently iterated item is a directory, then we recall the function with mentioning this new directory in order to execute the task all over the directory tree

			file = path.join(directory, file)
			renamer_destroyer(file)
		else:
			# If the currently iterated item is neither a file nor a directory, then we display the raise the error with a custom message

			raise TypeError(f'{file} is neither recognized as a file nor as a directory.')

def main():
	# Asking the user for the directory location
	directory = input(blue + 'Enter the directory location : ' + yellow)
	print(defcol, end = '')

	# Asking the user whether to destroy or restore
	choice = input(blue + 'Choose any of the below options :\n1. Destroy filenames\n2. Restore filenames\n\nEnter your choice : ' + yellow)
	print(defcol, end = '')
	if choice == '1':
		# If the user choosed the option to destroy filenames, then we continue

		renamer_destroyer(directory)
		print(f'[ {green}Process completed{defcol} ]')
	elif choice == '2':
		# If the user choosed the option to restore filenames, then we continue

		renamer_restorer(directory)
		print(f'[ {green}Process completed{defcol} ]')
	else:
		# If the user choosed an unavailable option, then we raise a fucking error with a custom message

		raise ReferenceError(f'{choice} no such options available.')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses the CTRL+C key combo, then we exit the script

		exit()
	except Exception as e:
		# If there are any errors encountered during the process, then we continue to display the error message on the console screen and then exit

		print(red_rev + f'[ Error : {e} ]' + defcol)