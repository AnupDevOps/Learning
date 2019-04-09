'''
Created on Oct 16, 2018

@author: Anup Kumar Mishra
'''

print("Python Functions Example")
print("\n")
def printme(strn):
    print(strn)

printme("Hello Function World")

# Example 2

def changeme(mylist):
    mylist.append(56)
    mylist.append([101, 102, 103, 104])
    print("My original List")
    print(mylist)

mylist= [10,20,30];
changeme(mylist);
print("Print List Element under a list")
print(mylist[4][2])