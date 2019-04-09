def square(x):
    return x*x
sq=square(10)
print(sq)


# Required arugument
def printInfo(name, age):
    print("Name: ", name)
    print("Age: ", age)
    return
printInfo("jack", 30)

#Default Arguments
def printInfoDefault(name, age= 40):
    print("Name: ", name)
    print("Age: ", age)
    return
printInfoDefault("John")
printInfoDefault("Vikas", 50)


# Variable-length args

def printInfoVariableArgs(arg1, *varTuple):
    print(arg1)
    for var in varTuple:
        print(var)
    return

printInfoVariableArgs(100)
printInfoVariableArgs(10,1,2,3,4,5)


#LAMBDA FUNCTIONS
mylist = [2,3,5,9,22,23,34]
print(list(map(lambda x:x*4,mylist)))
print(list(filter(lambda x:x%3 == 0,range(2,100))))

print(list(filter(lambda x:x%3 == 0,mylist)))

total = lambda arg1,arg2: arg1 + arg2
print(total(100,10))



#Named Args
def printNamedInfo(**param):
    print(param)

printNamedInfo(x=1,y=2,z=3)

#Mix of all types
def printMix(x,y,*pospar,**keypar):
    print(x,y)
    print(pospar)
    print(keypar)

printMix(1,0,2,3,4,5,a=1,b=2,c=3)


#Keywords args

def printKeywordargs(name, age):
    print("Name: ", name)
    print("Age: ", age)
    return

printKeywordargs("jack",40)
printKeywordargs(age=50,name="john")
#printKeywordargs(40,"Jack")



# Global and Local variables

money = 5000
def addMoney():
    global money
    money = money + 1
    a = 5
    print(locals())
    print(globals())
addMoney()

