'''
Created on Oct 16, 2018

@author: training_d2.03.07
'''

a=10
b=20
# c=a+b
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a=60
b=13
c=a&b
print(c)

# If-Else
a=20
b=20

if a == b:
    print("True")
else:
    print("False")

# Another way
a=10
b=11
if (a is b):
        print("true")
else:
    print("False")

# Another way
a=10
b=10
if (id(a) == id(b)):
        print("True")
else:
    print("False")


a=10
b=20
if (a is not b):
        print("yes a is not b")
else:
    print("False")
    
a=10
b=10
if (a != b):
        print("yes a is not b")
else:
    print("False")
    
# In Operators in Python 
a=10
b=20
list1 = [1, 2, 3, 4, 5]

if (a in list1):
    print("A is there in list")
else:
    print(" A is not there in List")
    
a=5
if (a not in list1):
    print("A is not there in list Second loop")
else:
    print("A is there in list Second Loop")