"""
main.py - Mass Files Destroyer

This is the main script file which serves the entire functionality of the tool.

Author : Rishav Das (https://github.com/rdofficial/)
Created on : September 15, 2021

Last modified by : -
Last modified on : -

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Импорт необходимых функций и модулей
from os import rename, path, listdir
from base64 import b64encode
from sys import platform

# Проверка, поддерживаются ли цветовые коды или нет
if 'linux' in platform:
	# Если тип компьютера - линукс

	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	red_rev = '\033[07;91m'
	yellow_rev = '\033[07;93m'
	defcol = '\033[00m'
else:
	# Если тип компьютера не линукс

	red = ''
	green = ''
	yellow = ''
	blue = ''
	red_rev = ''
	yellow_rev = ''
	defcol = ''

# Объявление некоторых переменных, необходимых для этого скрипта
files = []

def listfiles(directory):
	""" Эта функция служит для вывода списка всех файлов во всем дереве директорияов. """

	# Проверка, является ли параметр каталогом или файлом
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

def destroyer(directory):
	""" Эта функция выполняет функцию уничтожения файлов в указанном пользователем директория. """

	# Загрузка всех файлов в дереве директории
	listfiles(directory)
	print(files)

	for file in files:
		# Итерации по каждому файлу

		# Чтение содержимого файла и преобразование кодировки
		contents = open(file, 'rb').read()
		contents = b64encode(contents)

		# Запись закодированного содержимого обратно в файл
		open(file, 'wb').write(contents)

		# Переименование файла
		# To be written later
		# rename(file, filename)
		# del filename

		# Отображение мессаге на экране консоли
		print(f'{green}[{red}!{green}] {yellow}{file}{defcol}')

def main():
	# Спросить пользователя о местонахождении директории
	directory = input(blue + 'Enter the directory location : ' + yellow)
	print(defcol, end = '')

	# Запуск функции "дестроер / destroyer()"
	destroyer(directory)

	# Отображение результата завершенного процесса на экране консоли
	print(f'[ Process completed ]')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# Если пользователь нажимает комбинацию клавиш CTRL+C, мы выходим из скрипта.

		exit()
	except Exception as e:
		# Если во время процесса возникают какие-либо ошибки, мы показываем сообщение об ошибке на экране консоли.

		print(f'[ Error : {e} ]')
		exit()
