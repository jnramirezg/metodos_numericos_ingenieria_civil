# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import NonUniformImage


# Linear x array for cell centers:
x = np.arange(0, 7)
y = np.arange(0, 7)

z = np.array([[4.8, 1.2, 2.5, 3.9, 2.0, 4.0, 0.4],
              [2.4, 2.0, 4.0, 1.0, 2.7, 1.0, 2.0],
              [1.1, 3.4, 0.8, 4.3, 1.9, 4.4, 4.0],
              [0.6, 4.0, 3.3, 2.0, 3.1, 2.0, 3.0],
              [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 1.0],
              [1.3, 1.2, 3.3, 4.7, 0.0, 3.2, 5.1],
              [0.1, 2.0, 0.3, 1.4, 0.4, 1.9, 6.3]])


x_map = np.ones((7,7))*x
y_map = (np.ones((7,7))*y).T

fig, ax = plt.subplots()
im = NonUniformImage(ax, interpolation='nearest', extent=(0, 7, 0, 7),
                     cmap='viridis')
im.set_data(x, y, z)
ax.add_image(im)

plt.plot(x_map, y_map,'k.')
ax.set_xlim(-0.5, 6.5)
ax.set_ylim(-0.5, 6.5)
ax.set_aspect('equal', adjustable='box')
ax.set_title('NonUniformImage class')