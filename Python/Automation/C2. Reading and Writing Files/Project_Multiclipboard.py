###################################################################################################################################################################################################
# 										Step 1: Comments and Shelf Setup
###################################################################################################################################################################################################
# Let’s start by making a skeleton script with some comments and basic setup.
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')


###################################################################################################################################################################################################
# 										Step 2: Save Clipboard Content with a Keyword
###################################################################################################################################################################################################
# The program does different things depending on whether the user want to save text to a keyword, load text into the clipboard, or list all the existing keywords.
# Save Clipboard Content. 

# If the first command line argument (which will always be at index of the sys.argv list) is 'save' u, the second command line argument is the 
# keyword for the current content of the clipboard. The keyword will be used as the key for mcbShelf, and the value will be the text currently on the clipboard
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
# List keywords and Load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	



mcbShelf.close()
