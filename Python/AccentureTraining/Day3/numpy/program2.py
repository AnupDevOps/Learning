# Line Graph using numpy

import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0,20,200)

# plot the data
plt.plot(x, x, label='linear')

# Add the legend
plt.legend()

# Show the plot
plt.show()
