# More on List

# Lists might contain items of different types, but usually the items all have the same type.

squares = [1, 4, 9, 16, 25]
print(squares)
print(type(squares))
# Indexing returns the items in list
print(squares[1])

# Negtive indexing is also possible in list
print(squares[-1])

# Silcing indexing in list
print(squares[-3:])

# All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:

print(squares[:])

# Lists also support operations like concatenation:
print(" New List after concatenation")
squares = squares + [36, 49, 64, 81, 100]
print(squares)

# List are mutable
# Mutable objects can change their value but keep their ID.
print("List are mutable")
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)

# You can also add new items at the end of the list, by using the append() method
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

# remove item from list
print("remove item from list")
cubes.remove(216)
print(cubes)

# change list size
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

# The built-in function len()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(len(letters))


# It is possible to nest lists (create lists containing other lists),
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][0])

# For loop in list
print("For loop in list")
for x in letters:
    print(x)

# IF loop in List:
print("IF loop in List:")
if 'x' in letters:
    print("Yes letter is there")
else:
    print("letter is not there")
# The pop() method removes the specified index, (or the last item if index is not specified):

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# Operation on Lists
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
##copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
###pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
##sort()	Sorts the list


print("clear list")
thislist.clear()
print(thislist)

print("Copy list")
thislist = ["apple", "banana", "cherry"]
copylist = thislist.copy()
print(copylist)
print(thislist)

print("Count List")
newlist = copylist+thislist
print(newlist)
print(newlist.count("banana"))

print("Extend list operation")
# Extend list with another list
list1 = ["101", "102", "103"]
list2 = ["book", "copy", "notebook"]
list1.extend(list2)
print(list1)

# Important
print("reverse list")
list2.reverse()
print(list2)

print("Sort List")
list2.sort()
print(list2)
