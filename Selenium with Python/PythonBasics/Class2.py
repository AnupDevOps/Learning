'''
Created on Oct 16, 2018

@author: training_d2.03.07
'''

class Foo():
    def bar(self, otherinstance):
        print(self is otherinstance)

# Self is like this in java
foo= Foo()
foo2= Foo()
foo.bar(foo2)
foo.bar(foo)

Foo.bar(foo, foo)