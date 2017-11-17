import numpy as np 

points = np.array([[1, 1], [8, 3], [6, 2]])
from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(points)

import matplotlib.pyplot as plt
voronoi_plot_2d(vor)
plt.show()