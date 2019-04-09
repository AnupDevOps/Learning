# Histogram

import numpy as np
import matplotlib.pyplot as plt


my_id_array=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[9,10,11,12]]]) 
plt.hist (my_id_array.ravel(), bins = 12, color="green")

plt.title("Frequency of my Array")
plt.xlabel("Element in array")
plt.ylabel("Number of ")

plt.show()
