# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:14:51 2021
https://stackoverflow.com/questions/56904546/how-to-add-information-to-a-scipy-spatial-voronoi-plot
@author: 57312
"""
import numpy as np
import matplotlib as mpl
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt


points = np.array([[ 10,  30],
                  [ 30, 120],
                  [ 50,  10],
                  [120,  40],
                  [-1000, -1000],
                  [-1000, 1000],
                  [1000,-1000],
                  [1000, 1000]
                  ])
vor = Voronoi(points)
PPT = np.array([60, 100, 40, 120])

# find min/max values for normalization
minima = min(PPT)
maxima = max(PPT)

# normalize chosen colormap
norm = mpl.colors.Normalize(vmin=minima, vmax=maxima, clip=True)
mapper = mpl.cm.ScalarMappable(norm=norm, cmap='viridis')


fig = plt.figure() 
ax = fig.add_subplot() 
voronoi_plot_2d(vor, ax=ax, show_vertices=False, point_size=10)


# colorize
for r in range(len(vor.point_region)):
    region = vor.regions[vor.point_region[r]]
    if not -1 in region:
        polygon = [vor.vertices[i] for i in region]
        plt.fill(*zip(*polygon), color=mapper.to_rgba(PPT[r]))
        

plt.xlim(0, 150)
plt.ylim(0, 150)


im = ax.imshow(np.linspace(minima, maxima, 100)*np.ones((100,100)), cmap='viridis')
ax.set_aspect('equal', adjustable='box')
#ax.set_title('NonUniformImage class')
fig.colorbar(im)
plt.show()

