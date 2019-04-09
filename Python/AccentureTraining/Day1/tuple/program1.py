print("tuple")
mytuple= (5,6,7)
print(mytuple)

mytuple=(10,10.8,"india")
print(mytuple)

#packing
mytuple= 1,2,3,"Pak"
print(mytuple)

#unpacking a Tuple
a,b,c,d = mytuple
print(a)
print(b)

print(type(mytuple))

mytuple= (10,20,30,40,50)
#mytuple[2] = 100
 
mytuple1= (10,20,30,40,50)
mytuple2= (60,70)
print(mytuple1 + mytuple2)

del mytuple1
print(mytuple1)
