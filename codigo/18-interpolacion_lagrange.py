# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 07:34:12 2021

@author: 57312
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')

xp = np.array([1.0, 2.0, 3.0, 4.0])
yp = np.array([1.0, 3.0, 2.0, 4.0])

m = len(xp)

pol = 0



for j in range(m):
    prod = 1
    for i in range(m):
        if i != j:
            prod = prod*(x-xp[i])/(xp[j]-xp[i])
    pol += prod*yp[j]
            

sp.expand(pol)


xe = np.linspace(1, 4, 100)
ye = 1.0*xe**3 - 7.5*xe**2 +17.5*xe - 10.0

fig = plt.figure() 
plt.plot(xe, ye)
plt.plot(xp, yp, 'k.')

for i in range(m):
    plt.annotate(f'(x{i+1}, y{i+1})', (xp[i] + 0.05, yp[i]+0.05))


plt.xlim(0, 5)
plt.ylim(0, 5)
plt.show()

