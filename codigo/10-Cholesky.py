# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:24:07 2021

@author: 57312
"""

# Matriz de coeficientes constantes.
A = [
     [ 6,  15, 55],
     [ 15,  55, 225],
     [ 55,  225, 979],
                     ]
# Vector de constantes.
B = [5, 9, 4, 2]

m = len(A)

# Se crea L como una matriz de ceros.
L = []
for i in range(m):
    L += [[]]
    for j in range(m):
            L[i] += [0]


for k in range(m):
    for i in range(k):      
        suma_tem = 0
        suma_tem += A[k][i]
        for j in range(i):
            suma_tem += -(L[i][j]*L[k][j])
        L[k][i] = (suma_tem/L[i][i])
    sum_tem = 0
    sum_tem += A[k][k]
    for j in range(k):
        sum_tem += -(L[k][j])**2
    L[k][k] = (sum_tem**0.5)
