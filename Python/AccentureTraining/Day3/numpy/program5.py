# Bar Chart

import matplotlib.pyplot as mt

y=[10,4,7,3,5,8,3]

v=len(y)

x=range(v)

width=1/1.5

mt.bar(x,y,width,color="red")
mt.ylabel("Price")
mt.xlabel("Product")
mt.show()
