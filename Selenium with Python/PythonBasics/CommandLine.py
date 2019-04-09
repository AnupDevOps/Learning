'''
Created on Oct 16, 2018

@author: training_d2.03.07
'''
import sys
args = sys.argv[1:]
progname = sys.argv[0]

# Progname is at 0 command line args
print(args, "program Excutting:\n", progname)
countofarg = len(args)
print(countofarg)
# sum =0
# for index in range(len(args)):
#   sum =sum+ args[index]
# print("Sum is ", sum)