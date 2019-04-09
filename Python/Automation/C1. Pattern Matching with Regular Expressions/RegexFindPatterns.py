import re	# Import the regex module with import re
def isNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True

print(isNumber('415-555-4234'))
print(isNumber('NotANumber'))
print(isNumber('45-555-4234'))

message = 'Call me at 415-555-4234 tomorrow, 415-555-4255 is my office'
for i in range(len(message)):
	chunk = message[i:i+12]
	if isNumber(chunk):
		print (' Phone number found:' +chunk)
print('Done')


#######################################################################################################################
# 		Do the same thing by using Regex 
#######################################################################################################################

#Create a Regex object with the re.compile() function. (Remember to use a raw string.)
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
mo = phoneNumRegex.search('My Number is 415-555-4242. Call me at 999-444-2222') 
# Call the Match object’s group() method to return a string of the actual matched text.
print("Phone Number Found: " + mo.group())


# More Pattern Matching with Regular Expressions

# Grouping with Parentheses

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My number is 415-222-3343.")
print ("Find Number by using Grouping with Parentheses")
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

# If you would like to retrieve all the groups at once, use the groups() method—note the plural form for the name.
print(mo.groups())

areacode, mainNumber = mo.groups()
print(" Area Code of the Phone number")
print(areacode)
print(" Main Number of the Phone number")
print(mainNumber)

# code to find number which have different Pattern

print("Different Phone Number")

# The \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters.
phoneNumRegex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My number is (415) 222-3343.")
print ("Find Number of Different Pattern")
print(mo.group())


#######################################################################################################################
# 				Matching Multiple Groups with the Pipe
#######################################################################################################################

# The | character is called a pipe

print("Matching Character by using Pipe")
heroRegex =  re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search("Batman and Tina Fey.")
print(mo1.group())

mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())

# say you wanted to match any of the strings 'Batman','Batmobile', 'Batcopter', and 'Batbat'.
try:
	print("Find From mutiple Character")
	batRegex = re.compile(r"Bat(man|Mobile|copter|bat)")
	mo = batRegex.search("Batbat lost the wheel")
	print(mo.group())
except:
	print("Error in String, Please check your character")

#######################################################################################################################
# 				Optional Matching with the Question Mark
#######################################################################################################################


try:
	batRegex = re.compile(r"Bat(wo)?man")
# The (wo)? part of the regular expression means that the pattern wo is an optional group
	mo = batRegex.search("The aventures of batman")
	print("Optional Matching with the Question Mark	")
	print(mo.group())
	
except:
	print("Optional Matching with the Question Mark is failling due to character missmatch")

# Example to find a phone number from optional way

print("Find Phone number from optional way")
phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mo = phoneRegex.search("My number is 234-8787")
print(mo.group())


#######################################################################################################################
# 				Matching Zero or More with the Star
#######################################################################################################################

# The * (called the star or asterisk) means “match zero or more”—the group that precedes the star can occur any number of times in the text.

print("\n")
print("Matching Zero or More with the Star")
batRegex = re.compile(r"Bat(wo)*man")
mo = batRegex.search("The Batman is ready")
print(mo.group())
mo = batRegex.search("The Batwoman is ready")
print(mo.group())
mo = batRegex.search("The Batwowowoman is ready")
print(mo.group())

#######################################################################################################################
# 				Matching One or More with the Plus
#######################################################################################################################

# While * means “match zero or more,” the + (or plus) means “match one or more.” Unlike the star, which does not require its group to appear in the matched string, the group preceding a plus must appear at least once.

print("\n")
print("Matching One or More with the Star")
batRegex = re.compile(r"Bat(wo)+man")

# The regex Bat(wo)+man will not match the string 'The Adventures of Batman' because at least one wo is required by the plus sign.
# mo = batRegex.search("The Batman is ready")
# print(mo.group())    # this will give error


mo = batRegex.search("The Batwoman is ready")
print(mo.group())
mo = batRegex.search("The Batwowowoman is ready")
print(mo.group())



#######################################################################################################################
# 				Matching Specific Repetitions with Curly Brackets
#######################################################################################################################

# If you have a group that you want to repeat a specific number of times, follow
# the group in your regex with a number in curly brackets. For example,
# the regex (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa',
# since the latter has only two repeats of the (Ha) group.

# the regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.

# (Ha){3,5}
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

haRegex = re.compile(r"(Ha){3}")
mo = haRegex.search("HaHaHa")
print(mo.group())

# mo = haRegex.search("Ha")   	# This will not work as 
print(mo.group())

#######################################################################################################################
# 					Greedy and Nongreedy Matching
#######################################################################################################################

# Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible.
# The nongreedy version of the curly brackets, which matches the shortest string possible, has the closing curly bracket followed by a question mark.

greedyHaRegex = re.compile(r"(Ha){3,5}")
mo = greedyHaRegex.search("HaHaHaHaHa")
print("Greedy example")
print(mo.group())


NongreedyHaRegex = re.compile(r"(Ha){3,5}?")
mo = NongreedyHaRegex.search("HaHaHaHaHa")
print("NonGreedy example")
print(mo.group())

#######################################################################################################################
# 					The findall() Method
#######################################################################################################################
# In addition to the search() method, Regex objects also have a findall() method. While search() will return a Match object of the first matched text in the searched string,
# the findall() method will return the strings of every match in the searched string.

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo=phoneRegex.search("Cell: 415-555-9999 Work: 615-782-8765")
print("Phone Number find" + mo.group())
print(mo.group())

# On the other hand, findall() will not return a Match object but a list of strings—as long as there are no groups in the regular expression.
# If there are groups in the regular expression, then findall() will return a list of tuples. Each tuple represents a found match, and its items are the 158 Chapter 7 matched strings for each group in the regex.

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
print(phoneRegex.findall("Cell: 415-555-9999 Work: 615-782-8765"))


print("Phone Number find by using FindAll Code")
phoneRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
print(phoneRegex.findall("Cell: 415-555-9999 Work: 615-782-8765"))

# To summarize what the findall() method returns, remember the following:
# 1. When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d, the method findall() returns a list of string matches, such as ['415-555-9999', '212-555-0000'].
# 2. When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\d\d\d), the method findall() returns a list of tuples of strings (one string for each group), such as [('415', '555', '1122'), ('212', '555', '0000')].

# Character Classes
# Shorthand 	character class Represents
# \d	 	Any numeric digit from 0 to 9.
# \D 		Any character that is not a numeric digit from 0 to 9.
# \w 		Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W 		Any character that is not a letter, numeric digit, or the underscore character.
# \s 		Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S 		Any character that is not a space, tab, or newline.

print("Find all words")
xmasRegex = re.compile(r"\d+\s\w+")
print(xmasRegex.findall("12 drunmmer, 11 pipes"))

# The regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+), followed by a whitespace character (\s),
# followed by one or more letter/digit/underscore characters (\w+). The findall() method returns all matching strings of the regex pattern in a list.

#######################################################################################################################
# 					Making Your Own Character Classes
#######################################################################################################################

# There are times when you want to match a set of characters but the shorthand character classes (\d, \w, \s, and so on) are too broad.

print("Matching Your own Character")
vowelRegex = re.compile(r"[aeiouAEIOU]")
print(vowelRegex.findall("RoboCop eats baby food. BABY FOOD."))

# By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class. A negative character class will match all the characters that are not in the character class.

print("Matching Your own Character with negative")
vowelRegex = re.compile(r"[^aeiouAEIOU]")
print(vowelRegex.findall("RoboCop eats baby food. BABY FOOD."))

#######################################################################################################################
# 					The Caret and Dollar Sign Characters
#######################################################################################################################
# You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. Likewise, you can
# put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern. And you can use the ^ and $ together to indicate that the entire string must match the regex

beginsWithHello = re.compile(r"^Hello")
print(beginsWithHello.search("Hello World"))
print(beginsWithHello.search("He said hello."))

# The r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9.

endsWithNumber = re.compile(r"\d$")
print(endsWithNumber.search("Your Number is 42"))
print(endsWithNumber.search("Your Number is two"))

# The r'^\d+$' regular expression string matches strings that both begin and end with one or more numeric characters.

print("Find the charcaters that begins and End with mattched pattern")
endsWithNumber = re.compile(r"^\d+$")
print(endsWithNumber.search("5423415"))
print(endsWithNumber.search("Your Number is two"))

#######################################################################################################################
# 					The Wildcard Character
#######################################################################################################################
# The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.

print("The Wildcard Character")
atRegex = re.compile(r".at")
print(atRegex.findall("The car un the hat sath on the flat mat"))

#######################################################################################################################
# 					Matching Everything with Dot-Star
#######################################################################################################################

# Sometimes you will want to match everything and anything. For example, say you want to match the string 'First Name:', followed by any and all text, followed by 'Last Name:', and then followed by anything again.

print("Matching Everything with Dot-Star")
nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
print(nameRegex.findall("First Name: ANup Last Name: Mishra"))
print(nameRegex.search("First Name: ANup Last Name: Mishra").group())

# The dot-star uses greedy mode: It will always try to match as much text as possible. To match any and all text in a nongreedy fashion, use the dot, star, and question mark (.*?).

print("Greedy and NonGreedy tasks")
nongreedyRegex = re.compile(r"<.*?>")
mo = nongreedyRegex.search("<To serve Man> for dinner.>")
print(mo.group())

greedyRegex = re.compile(r"<.*>")
mo = greedyRegex.search("<To serve Man> for dinner.>")
print(mo.group())
####################################################################################################################### 27th September 2018 Page number 161#######################################################################################################################

#######################################################################################################################
# 					Matching Newlines with the Dot Character
#######################################################################################################################

print("Matching Newlines with the Dot Character")
# The dot-star will match everything except a newline. By passing re.DOTALL as the second argument to re.compile(), you can make the dot character match all characters, including the newline character.

nonewLineRegex = re.compile(".*")
print(nonewLineRegex.search("Serve the public trust.Protect the innocent.\n uphold the law.").group())

# matching all the lines in one run

print("\n")
print("matching all the lines in one run")
nonewLineRegex = re.compile(".*", re.DOTALL)
print(nonewLineRegex.search("Serve the public trust. \nProtect the innocent.\n uphold the law.").group())

# The regex noNewlineRegex, which did not have re.DOTALL passed to the re.compile() call that created it, will match everything only up to the first
# newline character, whereas newlineRegex, which did have re.DOTALL passed to re.compile(), matches everything. This is why the newlineRegex.search() call matches the full string, including its newline characters.

#######################################################################################################################
# 						Review of Regex Symbols
#######################################################################################################################

# This chapter covered a lot of notation, so here’s a quick review of what you learned:
# • The ? matches zero or one of the preceding group.
# • The * matches zero or more of the preceding group.
# • The + matches one or more of the preceding group.
# • The {n} matches exactly n of the preceding group.
# • The {n,} matches n or more of the preceding group.
# • The {,m} matches 0 to m of the preceding group.
# • The {n,m} matches at least n and at most m of the preceding group.
# • {n,m}? or *? or +? performs a nongreedy match of the preceding group.
# • ^spam means the string must begin with spam.
# • spam$ means the string must end with spam.
# • The . matches any character, except newline characters.
# • \d, \w, and \s match a digit, word, or space character, respectively.
# • \D, \W, and \S match anything except a digit, word, or space character, respectively.
# • [abc] matches any character between the brackets (such as a, b, or c).
# • [^abc] matches any character that isn’t between the brackets.

#######################################################################################################################
# 						Case-Insensitive Matching
#######################################################################################################################

# Normally, regular expressions match text with the exact casing you specify.

regex1= re.compile("RoboCop")
regex2= re.compile("ROBOCOP")
regex3= re.compile("robOcop")
regex4= re.compile("RobocOP")

# To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().
robocop = re.compile(r"robocop", re.I)
print(robocop.search("RobocOP is part man, part machine all cop.").group())

print(robocop.search("ROBOCOP is part man, part machine all cop.").group())

#######################################################################################################################
# 						Substituting Strings with the sub() Method
#######################################################################################################################

# Regular expressions can not only find text patterns but can also substitute new text in place of those patterns. The sub() method for Regex objects is
# passed two arguments. The first argument is a string to replace any matches. The second is the string for the regular expression. The sub() method returns a string with the substitutions applied.

print("\n")
print("Substituting Strings with the sub() Method")
namesRegex = re.compile(r"Agent \w+")
print(namesRegex.sub("CENSORED", "Agent Alice gave the secret document to Agent Bob"))

#######################################################################################################################
# 						Managing Complex Regexes
#######################################################################################################################

# You can mitigate this by telling the re.compile() function to ignore whitespace and comments inside the regular expression string. This “verbose mode” can be enabled by passing the variable re.VERBOSE as the second argument to re.compile().\

# Now instead of a hard-to-read regular expression like this:
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# you can spread the regular expression over multiple lines with comments like this:

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
\d{3}
(\s|-|\.)
\d{4}
(\s*(ext|x|ext.)
\s*\d{2,5})?
)''', re.VERBOSE)

# Note how the previous example uses the triple-quote syntax (''') to create a multiline string so that you can spread the regular expression definition over many lines, making it much more legible.

#######################################################################################################################
# 						Combining re.IGNOREC ASE, re.DOT ALL , and re.VERBOSE
#######################################################################################################################

# Unfortunately, the re.compile() function takes only a single value as its second argument. You
# can get around this limitation by combining the re.IGNORECASE, re.DOTALL, and re.VERBOSE variables using the pipe character (|), which in this context is known as the bitwise or operator.

# So if you want a regular expression that’s case-insensitive and includes newlines to match the dot character, you would form your re.compile() call like this:

someRegexValue = re.compile("foo", re.IGNORECASE | re.DOTALL | re.VERBOSE)
print(someRegexValue.findall("FOO is foo"))
print(someRegexValue.search("FOO is foo").group())





























