"""
renamer.py - Mass Files Destroyer

This script serves the functionality of renaming the files listed in the user specified directory. The script uses the encoding changing method in order to rename the files. This script defines two important functions : renamer_destroyer, rename_restorer. Both of the functions works under the renaming algorithm, but result of both are opposite. The renamer_destroyer() function renames the file from the original format to the base64 format and thus destroying the original name of it. On the other hand, the renamer_restorer() function restores the original name by changing the encoding of the base64 format filename back to the original utf-8 format.

Created by : Rishav Das (https://github.com/rdofficial/)
Created on : September 17, 2021

Last modified by : -
Last modified on : -
"""

# Importing the required functions and modules
from os import path, rename, listdir
from base64 import b64encode, b64decode

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
		elif path.isdir(file):
			# If the currently iterated item is a directory, then we recall the function with mentioning this new directory in order to execute the task all over the directory tree

			file = path.join(directory, file)
			renamer_destroyer(file)
		else:
			# If the currently iterated item is neither a file nor a directory, then we display the raise the error with a custom message

			raise TypeError(f'{file} is neither recognized as a file nor as a directory.')