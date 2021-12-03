# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:48:57 2021

@author: 57312
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import NonUniformImage
from mpl_toolkits.mplot3d.axes3d import Axes3D

X=0
Y=1

estacion = np.array([[ 10,  30],
                     [ 30, 120],
                     [ 50,  10],
                     [120,  40],
                     [80, 80]
                               ])

PPT = np.array([60, 100, 40, 100, 1000])


res = 1.01
x = np.arange(0, 140, res)
y = np.arange(0, 140, res)

n_cuad = len(x)

x_map = np.ones((n_cuad, n_cuad))*x
y_map = (np.ones((n_cuad, n_cuad))*y).T

w  = np.zeros((n_cuad, n_cuad))
for i in range(len(estacion)):
    dist = ((x_map-estacion[i][X])**2 +(y_map-estacion[i][Y])**2)**0.5
    w += 1/(dist)**2

PPT_i  = np.zeros((n_cuad, n_cuad))
for i in range(len(estacion)):
    dist = ((x_map-estacion[i][X])**2 +(y_map-estacion[i][Y])**2)**0.5
    PPT_i += PPT[i]/(dist**2*w )

fig, ax = plt.subplots()
im = NonUniformImage(ax, interpolation='nearest', extent=(0, 140, 0, 140),
                     cmap='viridis')
im.set_data(x, y, PPT_i)
ax.add_image(im)

#plt.plot(x_map, y_map,'k.')
plt.xlim(0,150)
plt.ylim(0,150)
ax.set_aspect('equal', adjustable='box')
#ax.set_title('NonUniformImage class')

plt.colorbar(im, ax=ax)


# Dibujar superficie 3D
fig = plt.figure()

axes3d = Axes3D(fig)

X,Y = np.meshgrid(x,y)

axes3d.plot_surface(X,Y, PPT_i, cmap="viridis")