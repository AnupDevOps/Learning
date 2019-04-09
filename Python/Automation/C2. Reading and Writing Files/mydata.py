###################################################################################################################################################################################################
# 										Saving Variables with the shelve Module
###################################################################################################################################################################################################
# You can save variables in your Python programs to binary shelf files using the shelve module. This way, your program can restore data to variables from the hard drive. 
# The shelve module will let you add Save and Open features to your program.

import shelve
shelfFile = shelve.open('mydata')    # mydata should need to be file name as well. Otherwise it will show you error. 
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

# After running the previous code on Windows, you will see three new files in the current working directory: mydata.bak, mydata.dat, and mydata.dir. On OS X, only a single mydata.db file will be created.

# These binary files contain the data you stored in your shelf. The format of these binary files is not important; you only need to know what the shelve module does, not how it does it. 
#The module frees you from worrying about how to store your program’s data to a file.

# Your programs can use the shelve module to later reopen and retrieve the data from these shelf files. Shelf values don’t have to be opened in read or write mode—they can do both once opened
shelfFile = shelve.open("mydata")
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

# Here, we open the shelf files to check that our data was stored correctly. Entering shelfFile['cats'] returns the same list that we stored earlier, so we know that the list is correctly stored, and we call close().

# Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys and values in the shelf.

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()


###################################################################################################################################################################################################
# 										Saving Variables with the pprint.pformat() Function
###################################################################################################################################################################################################
# If you import the pprint module into your programs, you’ll have access to the pprint() and pformat() functions that will “pretty print” a dictionary’s values. This is helpful when you want a cleaner display of the items in a dictionary than what print() provides.

print("\n")
print("Print by using PPrint")
import pprint
message = "it was a bright cold day in April, and the clocks were striking thirteen."
count = {}
for character in message:
	count.setdefault(character, 0)
	count[character] = count[character]+1
	
pprint.pprint(count)

# The pprint.pprint() function is especially helpful when the dictionary itself contains nested lists or dictionaries.

# If you want to obtain the prettified text as a string value instead of displaying it on the screen, call pprint.pformat() instead. These two lines are equivalent to each other:

# pprint.pprint(someDictionaryValue)
# print(pprint.pprint(someDictionaryValue))

# cats = [{'name': 'Zophie', 'desc': 'chubby'},{'name': 'Pooka', 'desc': 'fluffy'}
# pprint.pformat(cats)
# fileObj = open('myCats.py', 'w')
