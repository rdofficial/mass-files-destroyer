## Mass Files Destroyer

This tool serves the functionality of destroying files in an user specified directory tree. The contents of the files are replaced with some unreadable characters thus making the entire file seeming to be unworkable and corrupt. The files after the destruction may be able to be restored using the restore.py script, but sometimes due to some internal errors the files may get lost forever. Thus, use this tool at your own risk. The script is written in python3 programming language.

__Dependencies :__
The script only requires python3 to be installed in your computer in order to work properly. No other external python modules are required in order for the task to be executed during the process.

__Setup :__
1. Using the terminal, type the following code and press enter. ```git clone https://github.com/rdoficial/mass-files-destroyer.git/```
2. Then, the entire repository is cloned in the current working directory, just cd into that directory and launch the script.
3. Use the script only at your own risk.

__Usage :__
The _main.py_ is the file that we will use. Just launch the script, and it will continue asking for the directory location where we wan't to execute the attack. The project also contains several other script files that serve miscallenous tasks. Those script files are stored in the scripts/ sub-folder. The usage of each files are listed below :

* _restore.py_ : The script serves the functionality of restoration of those directories which are destroyed / corrupted by the main.py file's execution. The script on launching will ask for the required directory for the restoration purpose.
* _renamer.py_ : The script serves the functionality of destroying the filenames of an entire directory tree, as well restoration too. The script on launching will ask for the directory location as well as whether to destroy or restore.

### Note

The script is made for testing and fun purposes. Use it only for educational purposes, and make sure that no one is harmed using these scripts. The scripts may be dangerous and can be used for harmful deeds if used in a proper way. Be aware of it.

### About the author

This project is created by [Rishav Das](https://github.com/rdofficial/), on September 15, 2021.