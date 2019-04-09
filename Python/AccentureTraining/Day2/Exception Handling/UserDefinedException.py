# UserDefinedException.py

import unittest
class StudExcept(Exception):
    def __init__(self, msg='unknown error', errnum = 1):
        self.msg = msg
        self.errnum = errnu

    def printDetails():
        print(self.msg,self.errnum)

class Student:
    def __init__(self, *p):
        if len(p) == 0:    #Default Constructor
            self.marks = 0
            self.garde = 0
            self.name = ''
            self.id = ''
        elif len(p) < 4: raise IndexError("Not Enough vaues")
        else:
            if p[0] < 0: raise StudExcept("Marks in Negtive",1)
            else: self.marks = p[0]
            if p[1] < 1: raise StudExcept("grade in less than one",2)
            else: self.garde = p[1]
            if not isinstance(p[2],str):
                raise StudExcept('',3)
            else: self.name = p[2]
            if not isinstance(p[3],str):
                raise StudExcept('',4)
            else: self.name = p[3]

    def PrintDetails(self):
        print(self.marks,self.garde,self.id, self.name)


#try:
#    stud1 = Student(90,-2,'ANup','102')
#except StudExcept as e:
#    e.PrintDetails()
#except IndexError as e:
#   print(e)

class StudentTestClass(unittest.TestCase):
    def setUp(self):
        print("Entering Student Test case")


    def testDefConstructor(self):
        a = Student()
        self.assertTrue(a.marks == 0)
        self.assertTrue(a.garde == 0)
        self.assertTrue(a.name == '')
        self.assertTrue(a.id == '')

    def testParamConst(self):
        a = Student(80,1,'Jack','102')
        self.assertEqual(a.marks, 80)
        self.assertEqual(a.name, 'Jack')
        self.assertEqual(a.garde, 1)
        self.assertEqual(a.id, '102')

    def tearDown(self):
        print("Done with UnitTest")

unittest.main()
        
