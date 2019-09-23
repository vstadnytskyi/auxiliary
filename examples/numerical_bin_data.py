
from ubcs_auxiliary.numerical import bin_data
from numpy import random, arange
from pdb import pm
data = random.rand(1000,4)+ 1
x = arange(0,data.shape[0],1)
binned_data = bin_data(data  = data, x = x, num_of_bins = 100, dtype = 'float')

import matplotlib.pyplot as plt
fig, [ax1, ax2] = plt.subplots(nrows=2, ncols=1)
ax1.plot(x,data[:,0],'-')
ax2.fill_between(binned_data['x'], binned_data['y_min'][0], binned_data['y_max'][0], color='grey', alpha='0.5')
ax2.plot(binned_data['x'],binned_data['y_mean'][0],'-')
fig.show()
