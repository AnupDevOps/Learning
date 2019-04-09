# Class and Object

class Employee:
    """
    This is a employee class
    """
    
    empcount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1


    def DisplayName(self):
        print("Name: ",self.name)
        print("salary: ",self.salary)


# Create Object

emp1 = Employee("john", 10000)
emp2 = Employee("Jack", 50000)

emp1.DisplayName()
emp2.DisplayName()

print(" Total Employees %d"%Employee.empcount)


emp1.age = 7

hasattr(emp1, 'age') #Checking the attribute
hasattr(emp2, 'age') #Checking the attribute

getattr(emp1, 'age') # Check its value
setattr(emp1,'age',10)
hasattr(emp1, 'age')

hasattr(emp1, 'age')


print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
