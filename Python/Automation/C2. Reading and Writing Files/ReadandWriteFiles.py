
###################################################################################################################################################################################################
# 										Chapter 2: Reading and Writing Files
###################################################################################################################################################################################################

# Backslash on Windows and Forward Slash on OS X and Linux

# On Windows, paths are written using backslashes (\) as the separator between folder names. OS X and Linux, however, use the forward slash (/)
# as their path separator. If you want your programs to work on all operating systems, you will have to write your Python scripts to handle both cases. Fortunately, this is simple to do with the os.path.join() function.

import os
print(os.path.join('usr','bin','spam'))

# The os.path.join() function is helpful if you need to create strings for filenames. These strings will be passed to several of the file-related functions introduced in this chapter.

myFiles = ['account.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print(os.path.join("C:\\Users\\anup.b.kumar.mishra", filename))
	
# The Current Working Directory

print("The Current Working Directory")
print(os.getcwd())

# You can get the current working directory as a string value with the os.getcwd() function and change it with os.chdir(). Enter the following into the interactive shell

os.chdir("C:\\Windows\\System32")
print(os.getcwd())



###################################################################################################################################################################################################
# 										Absolute vs. Relative Paths
###################################################################################################################################################################################################

# An absolute path, which always begins with the root folder    
# A relative path, which is relative to the program’s current working directory
# There are also the dot (.) and dot-dot (..) folders. These are not real folders but special names that can be used in a path. A single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) means “the parent folder

###################################################################################################################################################################################################
# 										Creating New Folders with os.makedirs()
###################################################################################################################################################################################################

# os.makedirs('C:\\Users\\anup.b.kumar.mishra\\Desktop\\Python\\Automation\\myfolder')

# error: Don't use single backslashes(\) use double backslashes(\\)

###################################################################################################################################################################################################
# 										The os.path Module
###################################################################################################################################################################################################

# The os.path module contains many helpful functions related to filenames and file paths. For instance, you’ve already used os.path.join() to build paths in a way that will work on any operating system. Since os.path is a
# module inside the os module, you can import it by simply running import os. Whenever your programs need to work with files, folders, or file paths, you can refer to the short examples in this section.

# Handling Absolute and Relative Paths

# The os.path module provides functions for returning the absolute path of a relative path and for checking whether a given path is an absolute path.
# Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.
# Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path. 
# Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.

print("\n")
print("Handling Absolute and Relative Paths")
print(os.path.abspath('.'))

print(os.path.abspath('.\\automation'))

print(os.path.isabs('.'))

print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath("c:\\Windows", "C:\\"))

print(os.path.relpath("c:\\Windows", "C:\\spam\\eggs"))

print(os.getcwd())

# Calling os.path.dirname(path) will return a string of everything that comes before the last slash in the path argument. Calling os.path.basename(path) will return a string of everything that comes after the last slash in the path argument.

path = "C:\\Windows\\System32\\cal.exe"

# print(os.path.basename(path))

# print(os.path.dirname(path))

# If you need a path’s dir name and base name together, you can just call os.path.split() to get a tuple value with these two strings

print(os.path.split(path))

# But os.path.split() is a nice shortcut if you need both values

# To get all files name under a folder use os.path.join(os.path.dirname(filepath), filename)

print("\n")
print("\n")
print("Get Folder and files name together")
print(os.path.join("C:\\Users\\anup.b.kumar.mishra\\Desktop\\Python\\Automation", filename))

###################################################################################################################################################################################################
# 										Finding File Sizes and Folder Contents
###################################################################################################################################################################################################
# Once you have ways of handling file paths, you can then start gathering information about specific files and folders. The os.path module provides functions for finding the size of a file in bytes and the files and folders inside a given folder.
# Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.
# Calling os.listdir(path) will return a list of filename strings for each file in the path argument. (Note that this function is in the os module, not os.path.)


filepath = "C:\\Users\\anup.b.kumar.mishra\\Desktop\\Python\\Automation\\Automation.py"

print(os.path.getsize(filepath))

print(os.listdir(os.path.dirname(filepath)))

# If I want to find the total size of all the files in this directory, I can use os.path.getsize() and os.listdir() together.

totalsize = 0
for filename in os.listdir(os.path.dirname(filepath)):
	totalsize =  totalsize+ os.path.getsize(os.path.join(os.path.dirname(filepath), filename))
	
print("Total size of all files")
print(totalsize)

###################################################################################################################################################################################################
# 										Checking Path Validity
###################################################################################################################################################################################################

# Calling os.path.exists(path) will return True if the file or folder referred to in the argument exists and will return False if it does not exist.
# Calling os.path.isfile(path) will return True if the path argument exists and is a file and will return False otherwise.
# Calling os.path.isdir(path) will return True if the path argument exists and is a folder and will return False otherwise.

print("\n")
print("Checking Path Validity")
print(os.path.exists("C:\\Windows"))

print(os.path.exists("C:\\some_made_up_Folder"))

print(os.path.isdir("C:\\Windows"))

print(os.path.isdir("C:\\some_made_up_Folder"))

filepath = "C:\\Users\\anup.b.kumar.mishra\\Desktop\\Python\\Automation\\Automation.py"
print(os.path.isfile(filepath))

# You can determine whether there is a DVD or flash drive currently attached to the computer by checking for it with the os.path.exists() function. For instance, if I wanted to check for a flash drive with the volume named D:\ on my Windows computer

print("DVD or flash drive")
print(os.path.exists("D:\\"))

###################################################################################################################################################################################################
# 										The File Reading/Writing Process
###################################################################################################################################################################################################

# There are three steps to reading or writing files in Python.
# 1. Call the open() function to return a File object.
# 2. Call the read() or write() method on the File object.
# 3. Close the file by calling the close() method on the File object.

# Opening Files with the open() Function

print("\n")
print("Opening Files with the open() Function")
password = open("C:\\Users\\anup.b.kumar.mishra\\Desktop\\Python\\Automation\\SecretPasswordfile.txt")

print(password)

# Reading the Contents of Files

print("\n")
print("File content")
content = password.read()
print(content)

# If you think of the contents of a file as a single large string value, the read() method returns the string that is stored in the file.
# Alternatively, you can use the readlines() method to get a list of string values from the file, one string for each line of text.

demof = open("C:\\Users\\anup.b.kumar.mishra\\Desktop\\Python\\Automation\\demofile.txt")
print(demof.readlines())

###################################################################################################################################################################################################
# 										Writing to Files
###################################################################################################################################################################################################
# Python allows you to write content to a file in a way similar to how the print() function “writes” strings to the screen. You can’t write to a file you’ve opened in read mode, though. Instead, 
# you need to open it in “write plaintext” mode or “append plaintext” mode, or write mode and append mode for short.
# Write mode will overwrite the existing file and start from scratch, just like when you overwrite a variable’s value with a new value. Pass 'w' as the second argument to open() to open the file in write mode.

Demofilename = "C:\\Users\\anup.b.kumar.mishra\\Desktop\\Python\\Automation\\demofile.txt"
demof = open(Demofilename, 'w')
demof.write("Hello World! \n")
demof.close()

demof = open(Demofilename, 'a')
demof.write("Bacon is not a vegetable")

demof.close()
demof = open(Demofilename)
content = demof.read()
demof.close()
print(content)






