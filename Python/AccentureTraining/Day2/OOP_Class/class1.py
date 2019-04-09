# Class in Python

class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

complexobj = Complex(4.5,8.5)
print(complexobj.real)
print(complexobj.imag)


# Class and Instance Variables

class Animal:
    kind = 'carnivore' # Class variable shared by all instances
    def __init__(self, name):
        self.name = name # Instance variable to each instance

tigerobj = Animal('Tiger')
lionobj = Animal('Lion')

print(tigerobj.kind)
print(lionobj.kind)
print(lionobj.name)
print(tigerobj.name)
