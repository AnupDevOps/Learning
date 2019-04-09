# Operator Overloading

class Vector:

    def __init__(self,a,b):
        self.a = a
        self.b = b


    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)


v1 = Vector(10,10)
v2 = Vector(120,110)
v3 = Vector(0,0)

v3 = v1+v2

print(v3.a,v3.b)
print(v3)
