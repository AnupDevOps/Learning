'''
Created on Oct 16, 2018

@author: Anup Kumar Mishra
'''
from _operator import index

# a=int(input("Enter A"))
# b=input("Enter B")
a=5
b=6
c=a+b
print("Sum is")
print(c)

# DATA Types
print("\n")
var1=1
var2='Hello World'
Var3="Python programming"
var1=2
print(var1, var2, Var3)

# List Data types in Python
print("\n")
print("List Data types example")
list1= ['Physics', 'Chemistry', 1997, 2000]
list2= [1, 2, 3, 4, 5]
list3= ["a", "b", "c"]
print(list1[3],"\n", list2, list3)
print(list1)
# Delete List 
del list1[3]
print(list1)
# Update List Value
print("\n")
print("Update List Value")
list3[2]="e"
print(list3)

# Tuple data type
# Element Inside the tuple are not able to update it.
print("\n")
print("Tuple data type")
tup1 = ("English", "Math", 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3= ("a", "b", "c")
print(tup1, tup2, tup3)
# trying to update the tuple
# tup3[2]="e"
# del tup3
print(tup3)

# Dictionary Data type
# Dictionary require Key and Value, both are of anytype
print("\n")
print("Dictionary Data type")
dictn= {'Name': 'Zarat', 'Age': 7, 'class': "3rd" }
print(dictn["Name"])
print(dictn["Age"])

# Strings in python
print("\n")
print("Strings in python")
str1="i am From LKM"
print(str1.isupper())
print(str1.capitalize())
index= str1.find("F")
print("Index is :", index)
print(str1.lower())
print(str1.upper())












































