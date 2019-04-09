#Python Hello World Command 
print('Hello World')
print('Would you like to see my first program')

if 5 > 2:
	print("five is greater than two")
#Try out comment here
	if 2 < 5:
		print("2 is less than 5")
		
#Python Variables
x=100
y="Anup"
print(x)
print(y)

#A variable is created the moment you first assign a value to it.
#Variables do not need to be declared with any particular type and can even change type after they have been set.
x=4
x="Changed the variable"
print(x)
#Variable Names
#A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)

#Remember that variables are case-sensitive

### Output Variable ###
#The Python print statement is often used to output variables.
#To combine both text and a variable, Python uses the + character:
x="Awesome"
print("Python is "+x)

#You can also use the + character to add a variable to another variable:
x="python is "
y="Awesome"
z=x+y
print(z)

#For numbers, the + character works as a mathematical operator:
x=10
y=5
print(x+y)

#If you try to combine a string and a number, Python will give you an error:
#wrong code
x=5
y="Hello"
#print(x+y)


##### Python Numbers #####
#There are three numeric types in Python:
# 	1.int
#	2.float
#	3.complex
#Variables of numeric types are created when you assign a value to them:

x=2
y=2.8
z=1j

print(x)
print(y)
print(z)

#To verify the type of any object in Python, use the type() function:
print(type(x))
print(type(y))
print(type(z))

#Int
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

#Float
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

#complex
#Complex numbers are written with a "j" as the imaginary part:

######## Python Casting  #########


#Specify a Variable Type
#There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
#Casting in python is therefore done using constructor functions:
#int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number) literal, or a string literal (providing the string represents a whole number)
#float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
#str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#########   Python Strings   ########

#String literals in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello".
#Strings can be output to screen using the print function. For example: print("hello").
#Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1])

#Substring. Get the characters from position 2 to position 5 (not included)

b = "Hello, World!"
print(b[2:5])

#The strip() method removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#The len() method returns the length of a string

a = "Hello, World!"
print(len(a))

#The lower() method returns the string in lower case
a = "Hello, World!"
print(a.lower())

#The upper() method returns the string in upper case
a = "Hello, World!"
print(a.upper())

#The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Capitalize string
b= "anup".capitalize() # output is Anup
print(b)

#check if variable is alpha or digit
"hello".isalpha() == True #output is true
"1234".isdigit() == True #output is true


###Important###
# very powerful function
######### Python format function  ##########
name="Anup"
machine="BOT"
print("Nice to meet you {0}. I am {1}".format(name,machine))

# Other of doing this 
print(f"Nice to meet you {name}. I am {machine}")


###################		Command-line String Input    	###################
#Python allows for command line input.
#That means we are able to ask the user for input.
#The following example asks for the user's name, then, by using the input() method, the program prints the name to the screen

print("Enter your name:")
x = input()
print("Hello, " + x)


print("hello world")
print("This is my program")


# Python Function example
def add_number(a, b):
    print(a + b)


add_number(10, 15)


# Python Type hinting
def add_numbers(a: int, b: int) -> int:
    # return a + b
    print(a + b)


add_numbers(12, 14)

b = "anup".capitalize()
print(b)

print("hello".isalpha())  # output is true
print("1234".isdigit())  # output is true

# Python format function  #
name = "Anup"
machine = "BOT"
print("Nice to meet you {0}. I am {1}".format(name, machine))

# Other of doing this
print(f"Nice to meet you {name}. I am {machine}")

# Boolena and None
python_course = True
java_course = False
print(int(python_course))
print(int(java_course))
print(str(java_course))

Aliens_found = None
print(Aliens_found)

# If statement
print("Type a number")
# number = input()
# number=int(number)
number = 3
if number <= 0:
    print("Number is Negative")
else:
    print("Number is positive")

# Truthy and falsy values
number = 5
if number:
    print("Number is define and truthy")

text = "pyhthon"
if text:
    print("text is define and truty")

# not if
number = 5
if number != 4:
    print("this will not execute")

python_course = True
if not python_course:
    print("This will also not Exevute")

# Multiple if conditions by using And and or
number = 3
text = "python"
if number == 3 and text:
    print("This will work")

if number == 17 or text:
    print("This will Also work")

# ternary if statements
a=1
b=2
print("Bigger") if a > b else print("smaller")


# Lists in Python
student_names = []
student_names = ["mark", "Kat", "Jessica"]
print(student_names)
print(student_names[1]) # to see a list name

# if wanna get list from last we can use -1, -2 and so on
print(student_names[-1])

# List Functions
# to add new member in list we use function append

student_names.append("Anup")
print(student_names)

# to check if person is in list or not

print("Anup" in student_names)
print("neeraj" in student_names)

# To check list length

print(len(student_names))

# List slicing

print(student_names[1:])
print(student_names[1:-1])

# delete a member from the list with function
print("This member is deleted" +student_names[1])
del student_names[1]
print(student_names)

# Loops in Python
# For Loop

for name in student_names:
    print("Student name is {0}".format(name))

# For loops in Number
x = 0
for index in range(10):
    x=x+10
    print("number is {0}".format(x))

# for Loop like i=0 and i<10 we use range in which range take two variables
x = 10
for index in range(11, 15):
    x = x+2
    print("number is {0}".format(x))

# For loop with increment like i=0;i<=10;i++

range(5, 10, 2)

# First value is start point, end point, Increment loop number

# While Loops



# Create Class in Python
class Student:
    pass


# create instance in class
student = Student()

print(student)
# Output : <__main__.Student object at 0x058D8E90>


# Remember: Python Want us to use the first capital letter for class name
# and first lowercase letter for the functions and Variables.

new_student = Student()

print(new_student)

# Output : <__main__.Student object at 0x058DE7B0>

# Remember: Two Instances of the same classes are independent of each others. See outputs

