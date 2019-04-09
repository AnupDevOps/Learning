import re, pyperclip

###################################################################################################################################################################################################
# 										Step 1: Create a Regex for Phone Numbers
###################################################################################################################################################################################################

# First, you have to create a regular expression to search for phone numbers.
phoneRegex = re.compile(r"""(
	(\d{3}|\(\d{3}\))?		#AreaCode
	(\s|-|\.)?				#Separartor
	(\d{3})					# First 3 Digit
	(\s|-|\.)				#Separartor
	(\d{4})					# First 4 Digit
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	#extension
	)""", re.VERBOSE)
# The phone number separator character can be a space (\s), hyphen (-), or period (.)

# print(phoneRegex.search("phone number is 222-333-5676").group())


###################################################################################################################################################################################################
# 										Step 2: Create a Regex for Email Addresses
###################################################################################################################################################################################################
# You will also need a regular expression that can match email addresses

# Create Email Regex.
# print("Create Email Regex.")
emailRegex = re.compile(r"""(
	[a-zA-Z0-9._%+-]+		#UserName
	@						# @ Symbol
	[a-zA-Z0-9._%+-]+		#domain name
	(\.[a-zA-Z]{2,4})
	)""", re.VERBOSE)

# print(emailRegex.search("my email address is anup.kumar@yahoo.co.in").group())

###################################################################################################################################################################################################
# 										Step 2: Create a Regex for Email Addresses
###################################################################################################################################################################################################

# Now that you have specified the regular expressions for phone numbers and email addresses, you can let Python’s re module do the hard work of
# finding all the matches on the clipboard. The pyperclip.paste() function will get a string value of the text on the clipboard, and the findall() regex method will return a list of tuples.

# Find matches in clipboard text.

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])
	
# As you can see at u, you’ll store the matches in a list variable named matches. It starts off as an empty list, and a couple for loops. For the email addresses, you append group 0 of each match w. For the matched phone
# numbers, you don’t want to just append group 0. While the program detects phone numbers in several formats, you want the phone number appended to be in a single, standard format. The phoneNum variable contains a string
# built from groups 1, 3, 5, and 8 of the matched text v. (These groups are the area code, first three digits, last four digits, and extension.)


###################################################################################################################################################################################################
# 										Step 4: Join the Matches into a String for the Clipboard
###################################################################################################################################################################################################


# Copy results to the clipboard.
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')


###################################################################################################################################################################################################
# 										Step 4: Join the Matches into a String for the Clipboard
###################################################################################################################################################################################################

# Running the Program For an example, open your web browser to the No Starch Press contact page at http://www.nostarch.com/contactus.htm, press ctrl-A to select all the text on
# the page, and press ctrl-C to copy it to the clipboard.
















