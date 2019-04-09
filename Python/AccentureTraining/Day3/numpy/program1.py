# numpy attributes

import numpy as np

my_array = np.array([[1,2,3,4],[5,6,7,8]], dtype = np.int64)

# print Memory address

print(my_array.data)

print(my_array.shape)

print(my_array.dtype)

print(my_array.strides)

# Different ways to create numpy arrays

# Create an array of ones.

print("Create an array of ones.")
print(np.ones((3,4)))

# Create an array if Zeros
print("Create an array if Zeros")

print(np.zeros((2,3,4), dtype = np.int16))

# Create an array with random values

np.random.random((2,2))

# Create Empty array
print("Create Empty array")

print(np.empty((3,2)))

# Create full array

full_array = np.full((2,2),7)
print(full_array.data)

# Create array of evenly-spaced values

np.arange(10,25,5)

np.linspace(0,2,9)



#Load Numpy array from text files
#x,y,z = np.loadtxt('paris.txt',skiprows=1,unpack = True) ##when true the x=1 column ,y =2 column , z=3 coulm and when unpack=false it take x =1,2,3 column 
#print(x)
#print(y)

#print(z)

my_missing_array = np.genfromtxt('paris.txt',skip_header = 1,filling_values = -99)
print(my_missing_array)


print(my_array.ndim) 
print(my_array.size) # Return the size
print(my_array.itemsize)
print(my_array.nbytes)
print(len(my_array)) # Return Dimension

#Broadcasting

print("................................... Broadcasting ................................")
x = np.ones((3,4))
y = np.random.random((3,4))
x.shape
y.shape

print(x+y)
print(x-y)

y = np.arange(4)
print(y)
print(y.shape)


# Aggregate functions

print("...................................  Aggregate functions ................................")
print(my_array.sum())
print(my_array.min())
print(my_array.max())
print(my_array.mean())

print("................................... Slicing and Indexing ................................")

print(my_array[1])
print(my_array[1][2])
print(my_array[1,2])
print(my_array[0:2])

print(my_array[my_array < 4])
bigger_than_5 = (my_array > 5)
print(my_array[bigger_than_5])



# Transpose
print("................................... Transpose ................................")
print(np.transpose(my_array))


#revel
print("................................... ravel ................................")
x = np.ones((3,4))
z = x.ravel()
print(z)


#Append 1D array to my_array
print(my_array)
new_array = np.append(my_array, [7,8,9,10])
print(new_array)
