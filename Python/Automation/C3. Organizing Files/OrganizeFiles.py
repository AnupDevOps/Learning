###################################################################################################################################################################################################
# 										Chapter 3 : Organizing Files
###################################################################################################################################################################################################

# The shutil Module
# The shutil (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs. To use the shutil functions, you will first need to use import shutil.

# Copying Files and Folders
# The shutil module provides functions for copying files, as well as entire folders. Calling shutil.copy(source, destination) will copy the file at the path 
# source to the folder at the path destination. (Both source and destination are strings.) If destination is a filename, it will be used as the new name of the copied file.

import shutil, os
os.chdir('c:\\')
shutil.copy('c:\\spam.txt', 'c:\\work')
# above command copy the file from source to destination

shutil.copy('c:\\spam.txt', 'c:\\work\\spam2.txt')