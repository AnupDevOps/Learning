# Python Operators
# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# They are simple you can use like arthmetic operations

# Python Lists
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security

# List
thislist = ["Apple", "Mango", "Banana"]
print(thislist)
print(thislist[1])

thislist[1]="Fruits"
print(thislist)
print(thislist[1])

print(thislist[-1])

# loop through a list
print("Loop is starting from here")
for x in thislist:
	print(x)
	
#list lenght 

print(len(thislist))

# Add Item in List we use append function 
print("Add Item Example Start here")
print(thislist)
thislist.append("Carrot")
thislist.append("Orange")
print(thislist)

# To add an item at the specified index, use the insert() method
print("Add Item by using Insert() method")
thislist.insert(1, "Pineapple")
print(thislist)

# Remove Item 
# The remove() method removes the specified item:

thislist.remove("Pineapple")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified)

thislist.pop()
print(thislist)

# The del keyword removes the specified index:
del thislist[1]
print(thislist)

#it can also delete all list as well
# del thislist
# print(thislist)

# List Methods
# Method		Description
# append()	Adds an element at the end of the list
# clear()		Removes all the elements from the list
# copy()		Returns a copy of the list
# count()		Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()		Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()		Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()		Sorts the list

###################################################################################################################################################################################################

# Python Tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple = ("Car", "Auto", "Bus", "Train")
print(thistuple)
print(thistuple[1])

# Change tuple value 
# Once a tuple is created, you cannot change its values. Tuples are unchangeable.
# thistuple[1] = "Air"
# print(thistuple) 

# loop in tuple 
print("tuple loop start here")
for x in thistuple:
	print(x)

#tuple lenght
print("Tuple lenght is ")
print(len(thistuple))

# Add and Remove item 
# once tuple is create you can not add or remove item 

###################################################################################################################################################################################################

# Python Sets
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

thisset = {"Apple", "Mango", "orange"}
print(thisset)


# Note: Sets are unordered, so the items will appear in a random order.
# access Item 
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in thisset:
	print(x)

print("orange" in thisset)
print("banana" in thisset)

# Once a set is created, you cannot change its items, but you can add new items

# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.

thisset.add("banana")
print(thisset)

# lenght 

print(len(thisset))

# To remove an item in a set, use the remove(), or the discard() method.

thisset.remove("banana")
print(thisset)


###################################################################################################################################################################################################
# Python Dictionaries

# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
"brand": "ford",
"model": "Mustage",
"year": 1964
}

print(thisdict)

# Access items
print(thisdict["model"])
print(thisdict["year"])

# There are also a method called get() that will give you the same result:
print(thisdict.get("brand"))

# You can change the value of a specific item by referring to its key name:

thisdict["year"] = 2018
print(thisdict)

# loop in Dictionaries
for x in thisdict:
	print(x)



###################################################################################################################################################################################################
# If Else loop in python 

# program to check graeter number among three
print("Enter 3 numbers")
# x=input("Enter X")
# y=input("Enter Y")
# z=input("Enter Z")
x = 3
y = 2
z = 1
if x > y:
	if x > z:
		print("x is greater" )
	else:
		print("z is greater" )
else:
	if y > z:
		print("y is greater" )
	else:
		print("z is greater" )
		

# Elif
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition"

a = 33
b = 33
if b > a:
	print("b is greater than a")
elif a == b:
	print("a is equal to b")
	

# Short Hand If ... Else

print("A is greater") if a > b else print("equal")



###################################################################################################################################################################################################
# Python While Loops
		

# Python has two primitive loop commands:
# while loops
# for loops

i = 1
while i < 6: 
	print(i)
	i += 1

# Note: remember to increment i, or else the loop will continue forever.
# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
print("break statment start here")
i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
print("Continue statment start here")
i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)

###################################################################################################################################################################################################
# Python For Loops


# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming language, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
	
	
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)



for x in fruits:	
	print(x)
	if x == "banana":
		break
	
# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number

for x in range(6):
  print(x)
  
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2, 6):
  print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

for x in range(2, 30, 3):
  print(x)

  
###################################################################################################################################################################################################
# Recursion

# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Python Functions

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Create a function 
def myfunction():
	print("Hello, Welcome to Python")
	
	
# calling a Function
myfunction()

# Parameters

# Information can be passed to functions as parameter.
# Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.
# The following example has a function with one parameter (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def myfunction(name):
	print("My name is " +name)

myfunction("Anup")
myfunction("Neeraj")

# Default Parameter Value
# If we call the function without parameter, it uses the default value:

def myfunction(name = "default_name"):
	print("My name is " +name)

myfunction("Anup_default")
myfunction("Neeraj_default")
myfunction()

# Return Values

def myfunction(x):
	return 5*x
	
print(myfunction(3))
print(myfunction(9))

###################################################################################################################################################################################################
# Python Lambda

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
lambda arguments : expression
 

print("Start using lambda function from here")
x = lambda a : a+10
print(x(5))

# Lambda functions can take any number of arguments:

x = lambda a,b : a*b
print(x(5,6))

x = lambda a,b,c : a*b*c
print(x(4,5,2))

# Why Use Lambda Functions?

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunction(n):
	return lambda a: a*n

mydouble = myfunction(2)

print(mydouble(11))


###################################################################################################################################################################################################
# Python Arrays

# Arrays are used to store multiple values in one single variable.

cars = ["Ford", "Volvo", "BMW"]

# An array is a special variable, which can hold more than one value at a time.
# If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this.

print(cars[1])

# The Length of an Array
print("Lenght of an array")
print(len(cars))

# Loop in array

for x in cars:
	print(x)
	
# Add an array element
print("Add new element")
cars.append("Hero")
for x in cars:
	print(x)
	
###################################################################################################################################################################################################
# Python Classes and objects

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects

# Create a Class
class myclass:
	x="Hello class"

# Create object
	
p1 =  myclass()
print(p1.x)

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# The __init__() function is called automatically every time the class is being used to create a new object.

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belongs to the object.
# Let us create a method in the Person class.

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def myfun(self):
		print("Hello My Name is " +self.name)
		
p1 = Person("John", 36)

print(p1.name)
p1.myfun()

# The self parameter is a reference to the class itself, and is used to access variables that belongs to the class.

# The self Parameter
# The self parameter is a reference to the class itself, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties

p1.age = 40
print(p1.age)

# Delete object properties 

del p1.age 

###################################################################################################################################################################################################
# Python Modules

# What is a Module?
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.


###################################################################################################################################################################################################
# Python Datetime

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x) 

# Date Output

# The date contains year, month, day, hour, minute, second, and microsecond.
# The datetime module has many methods to return information about the date object.
# Here are a few examples, you will learn more about them later in this chapter.

print("year is ")
print(x.year)
print(x.strftime("%A"))

###################################################################################################################################################################################################
# Python JSON

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# Python has a built-in package called json, which can be use to work with JSON data.

import json

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# some json
x = '{"name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# The result is a python dictionaries
print(y["age"])


# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# A python object(dict)
x = {
	"name": "Anup",
	"age": 24,
	"city": "New York"
	}
	
# Convert into Json
y = json.dumps(x)

# the result is a JSON String:
print(y)


# You can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# Python	JSON
# dict		Object
# list		Array
# tuple		Array
# str		String
# int		Number
# float		Number
# True		true
# False		false
# None		null

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:

print(json.dumps(x, indent=4))

###################################################################################################################################################################################################
# Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

try:
	print(m)
except:
	print("An exception occurred")

# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error:

# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

try:
	print(n)
except NameError:
	print("Variable n is not defined")
except: 
	print("Something else went wrong")

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:

try:
	print("Hello")
except:
	print("something went wrong")
else:
	print("nothing went wrong")

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
	print(n)
except:
	print("Something went wrong")
finally:
	print("The try except is finished")

# This can be useful to close objects and clean up resources:

try: 
	f = open("demofile.txt")
	f.write("Hello world")
	
except:
	print("Something went Wrong when writing in file")
finally:
	f.close()









