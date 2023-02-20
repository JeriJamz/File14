#saw this on twitter thought it was cool

import matplotlib.pyplot as plt, numpy as np

#this will make random data
data =  np.random.randn(1000,5)

#make a 2d histogram
plt.hist2d(data[:,0], data[:,1],bins = 200)

#adding a color bar
plt.colorbar()

#shows the plot
plt.show()
