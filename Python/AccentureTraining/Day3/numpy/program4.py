#Pie Chart

import matplotlib.pyplot as py

clr=["red","green","blue","yellow"]

size=[25,30,30,15]

lab=["India","US","Japan","UK"]
exp=[0,0,0,0]

py.pie(x=size, labels=lab, colors=clr, explode= exp)
py.show()
