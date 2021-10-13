# -*- coding: utf-8 -*-
# Método de Gauss-Seidel
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-10-11
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
    
'''
A = [
     [  3, -0.1, -0.2],
     [0.1,    7, -0.3],
     [0.3, -0.2,   10],
                      ]

B = [7.85, -19.3, 71.4]

sol = [0, 0, 0]

for i in range(10):
    sol[0] = (B[0] - A[0][1]*sol[1] - A[0][2]*sol[2])/A[0][0]
    sol[1] = (B[1] - A[1][0]*sol[0] - A[1][2]*sol[2])/A[1][1]
    sol[2] = (B[2] - A[2][0]*sol[0] - A[2][1]*sol[1])/A[2][2]

