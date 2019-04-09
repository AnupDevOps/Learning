print("Starting List")
#Unlike strings, Lists are mutable squenece of objects"
a = [1,2,3]
print(a)
# List is hecterogenus
a = [1,"yes",3]
print(a)
print(a[1])
#lenght of a list
print("lenght of a list")
print(len(a))

a = [[1,2],3,[4,5]]
print(a)
print(a[0][0])
print(a[2][0])

# Check if element is there in list
print(3 in a)
print(2 in a) # False because 2 in another list
print(2 in a[0])

b = [7,8,[9,10]]
print(a+b)

print(a*3)

#print(a+100)
a=[[1,2],3,[4,5],100]
print(a)
a.append(400)
print(a)

a.insert(3,500)
print(a)

a.pop()
print(a)
a.pop(2)
print(a)


b=[8,9,10]
b.clear()
print(b)

print(a.index(500))

print(a.count(500))

a.reverse()
print(a)

b=[8,11,10]
a.extend(b)
print(a)

b.sort()
print(b)



# Negative Indexing
mylist = ["I","N","D","I","A"]
print(mylist[-1])
print(mylist[-3])

# Silicing of list
print(mylist[2:5])
