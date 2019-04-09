'''
Created on Oct 16, 2018

@author: training_d2.03.07
'''
while True:
    try:
        n=input("Enter a Number to validate")
        n=int(n)
        break
    except ValueError:
        print("Not a valid Integer! Please try again")
print("Successfully Enter the integer")

# Assertions Demo
def get_age(age):
    assert age > 0, "Age can't be negtive"
    print("Your age is :", age)
get_age(-9)