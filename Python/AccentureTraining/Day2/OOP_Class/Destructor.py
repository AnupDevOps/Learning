# Destorying the Object - __del__

class Foo(object):
    def __init__(self, id):
        self.id = id
        print(self.id, 'Born')


    def __del__(self):
        print(self.id, 'died')

x = Foo(1)
x = Foo(2) # Implicit Cell
d = Foo(3)  
d.__del__() # Explicit Cell
