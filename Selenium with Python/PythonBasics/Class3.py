'''
Created on Oct 16, 2018

@author: training_d2.03.07
'''

class Shark:
    def swim(self,num1, num2):
        print("The Shark is Swimming")
        return num1*num2
    def be_awesome(self):
        print("The Shark is being Awesome")

sammy= Shark()
sammy.be_awesome()
print(sammy.swim(10,20))