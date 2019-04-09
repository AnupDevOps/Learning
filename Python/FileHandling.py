###################################################################################################################################################################################################
# Python File Open

# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files


# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)



# Syntax
# To open a file for reading it is enough to specify the name of the file:
try:
	f = open("demofile.txt")
except:
	print("not able to open the file")
	
# The code above is the same as.
# f = open("demofile.txt", "rt")

# Python File Open
# Open a File on the Server
# Asume we have the following file, located in the same folder as Python.

try:
	f=open("demofile.txt", "r")
	print(f.read())
except:
	print("Not able to read the file")

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many character you want to return.

f = open("demofile.txt", "r")
print(f.read(5))

# Read Lines
# You can return one line by using the readline() method:

print("Read Lines from a Text file")
f = open("demofile.txt", "r")
print(f.readline())


# By looping through the lines of the file 

f = open("demofile.txt", "r")
for x in f:
	print(x)
	
	
###################################################################################################################################################################################################
# Pthon File write

# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

f =open("demofile.txt", "a")
f.write("Now the file has one more line !")

f =open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")



###################################################################################################################################################################################################
# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# Create a file called "myfile.txt":
# f = open("myfile.txt", "x")

# Create a new file if it does not exist:
try:
	f = open("myfile.txt", "w")
except FileExistsError:
	print("File already exist")
except:
	print("Known Error")
	
###################################################################################################################################################################################################
# Python Delete File

# To delete a file, you must import the OS module, and run its os.remove() function.
import os
# os.remove("myfile_new.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exist before you try to delete it.

import os
if os.path.exists("myfile_1.txt"):
	print("File exist")
	os.remove("myfile_1.txt")
else:
  print("The file does not exist")
  
  
# Delete Folder
# To delete an entire folder, use the os.rmdir() method: 

import os
try:
	os.rmdir("Demo")
except:
	print("Folder is not there")