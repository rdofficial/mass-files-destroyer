"""
restore.py - Mass Files Destroyer

This script serves the functionality of restoring the destroyed files by the main.py script of this project. Also note that if plain and undestroyed files are passed to this script, then those files might get damaged a bit instead of remaining untouched or unchanged.

Created by : Rishav Das (https://github.com/rdofficial/)
Created on : September 16, 2021

Last modified by : -
Last modified on : -
"""

# Importing the required functions and modules
from os import path, rename, listdir
from base64 import b64decode
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

# Defining some variables globally which are required by the script
files = []

def listfiles(directory):
	""" Эта функция служит для вывода списка всех файлов во всем дереве директорияов. """

	# Проверка, является ли параметр директория или файлом
	if path.isfile(directory):
		# Если параметр - файл, то продолжаем

		files.append(directory)
		return 0
	elif path.isdir(directory):
		# Если параметр - директория, то продолжаем

		for file in listdir(directory):
			# Перебор содержимого директория

			file = path.join(directory, file)

			if path.isfile(file):
				# Если итем - файл, то продолжаем

				files.append(file)
				continue
			elif path.isdir(file):
				# Если итем - директория, то продолжаем

				listfiles(file)
				continue
			else:
				# Если итем не является ни файлом, ни директория, тогда мы пропускаем текущую итерацию

				continue
	else:
		# Если параметр не является ни файлом ни директором, то мы показьваем эррор

		raise ValueError(f'{directory} is neither a file nor a directory')
		return 0

def restorer(directory):
	""" This function serves the functionality of restoration of the files which are destroyed by the main.py script file. Also, note that if normal files are passed to this function, then those files may get damaged too, instead of getting restored or being remained unchanged. """

	# Calling the listfiles() function to get the list of all the files in the directory tree
	listfiles(directory)

	for file in files:
		# Iterating over each file to restore it

		# Reading the contents of the destroyed file and then restoring it by changing the encoding from base64 to utf-8 back
		contents = open(file, 'rb').read()
		contents = b64decode(contents)

		# Saving the original contents of the file back to the file
		open(file, 'wb').write(contents)

		# Displaying the current iteration information on the console screen
		print(f'{green}[{red}!{green}] {yellow}{file}{defcol}')

def main():
	# Asking the user for the directory location
	directory = input(blue + 'Enter the directory location : ' + yellow)
	print(defcol, end = '')

	# Calling the restorer() function in order to start the restoration process
	restorer(directory)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses the CTRL+C key combo, then we exit the script

		exit()
	except Exception as e:
		# If there are any errors encountered during the process, then we continue to display the error message on the console screen and then exit

		print(red_rev + f'[ Error : {e} ]' + defcol)