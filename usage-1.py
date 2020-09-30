import matplotlib.pyplot as plt
import numpy as np
from ubcs_auxiliary import numerical
row = np.asarray([100, 200,400, 600, 150])
col = np.asarray([100, 200,300, 400, 300])
nn = numerical.nearest_neibhour(row = row, col = col)
plt.grid()
for i in range(len(nn[1])):
   plt.scatter(col[nn[1,i]],row[nn[1,i]], s=400, marker = f'${i}$')
plt.title('example: point 1')
plt.show()
