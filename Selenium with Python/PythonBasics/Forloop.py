'''
Created on Oct 16, 2018

@author: training_d2.03.07
'''
# For loop in other language
# for (i=0; i < 10; i++)
# range (start value, end value)
for i in range(10):
    print(i)

for i in range(0, 10, +2):
    print(i)
# Reverse For loop
print("Reverse Loop")
for i in range(10, 0, -1):
    print(i)
    
# letter in python will be treated as a variable
for letter in 'Python':
        print(letter) 
        
fruits = ["Banana", "Mango", "Apple"]
for fruit in fruits:
    print(fruit)
    print(len(fruits))


fruits = ["Banana", "Mango", "Apple"]
print(range(len(fruits)))
for index in range(1, len(fruits)):
    print(fruits[index])

# Sum of all the elements
values = [2,4,5,6,8,10]
add = 0
for index in range(len(values)):
    add= add+ values[index]
print("Sum is ", add)


# While loop

num=10
add=0
i=1

while i<=num:
    add=add+i
    i=i+1
print("Add is ", add)

