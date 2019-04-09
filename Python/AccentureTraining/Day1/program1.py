print("Hello")
print("Welcome to Accenture")
print(3*2)
type(10)
a = 100
if a== 101:
    print("value of a is 100")
else:
    print("Value of a is not 100")
print("good bye")

#ELif example
x = 10
y = 15
if x == y:
    print(x, "and",  y, "are equal")
else:
    if x < y:
        print(x, "is less than", y)
    else:
        print(y, "is less than", x)

# Add two number
print("Enter first Number")
#a=int(input())
a = 12
print("Enter Second Number")
#b=int(input())
b = 13
c=a+b
print("Sum is ", c)


# Loops in Python
print("Loops in Python")
count = 0
while(count < 4):
    print("The count is :", count)
    count = count + 1
print("Good Bye")

# For loop in Python
print("For loop in Python")
for letter in "Python":
    print(letter, end=" ")
fruits=["Banana", "Mango", "Apple"]   #list in python
for fruit in fruits:
    print("current fruit:", fruit)
print("Good bye")


# Activity 3
print(" Activity 3")

n=1
while (n <25):
    if(n%2 == 0):
        print(n)
    n=n+1

# using for loop
print("using for loop")
for n in range(1,25):
    if(n%2 == 0):
        print(n)

# factorial of a number
sum = 1
print("Enter a number")
#n=int(input())
n=5
print("number is", n)
for m in range(1,n+1):
    sum *= m 
print(sum)

# print in differenr format
print("factorial of %s is %s"%(n,sum))


#activity 4
# To DO
sum=0
print("enter a number ")
n=int(input())
while n > 0:
    m=n%10
    sqr = m**2
    sum=sum+sqr
    n = n / 10
print(sum)


