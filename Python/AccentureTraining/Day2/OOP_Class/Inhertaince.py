# INheritance.py

class Parent:
    parentattr = 100
    def __init__(self):
        print("Calling parent INit")

    def parentMethod(self):
        print("calling Parent Method")

    def SetAttr(self, attr):
        Parent.parentattr = attr

    def getAttr(self):
        print(Parent.parentattr)

    def myMythod(self):
        print("Parent Method")



class Child(Parent):
    def __init__(self):
        print("Calling Child Init")

    def childMethod(self):
        print("Calling Child Method")

    
    def myMythod(self):
        print("Child Method")


c = Child()
c.childMethod()
c.parentMethod()
c.SetAttr(200)
c.getAttr()
c.myMythod()
        
