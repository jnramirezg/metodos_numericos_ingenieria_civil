# -*- coding: utf-8 -*-
# Descomposición LU.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-10-18
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
    
'''

# %%Importación de librerías.
import numpy as np


# %%Definición de funciones.


def np_descomposicion_LU(A):
    '''
        Descomposición de la Matriz A en las matrices L y U con el método de la
        eliminación de Gauus. La matriz A se debe ingresar como una lista de
        listas. El programa por dentro requiere el módulo numpy.
        
        Devuelve L y U como np.array()
    '''
    m = len(A)
    L = np.eye(m, dtype=float)    # Se crea L como una matriz identidad.
    U = np.array(A, dtype=float)  # Se crea U como una copia de A.
    
    for k in range(m):
        U1 = np.array([f[:] for f in U])  # Copia de la matriz.
        for i in range(k+1, m):
           for j in range(m):
                pivote = U[k, k]
                U1[i, j] += -U[i, k]/pivote * U[k, j]
                if j==k:
                   L[i, j] = U[i, k]/pivote           
        U = U1
    
    return L, U


# %%Ejemplos

# Ejemplo 1.
A = [[ 2,  1, -1,  2],
     [ 4,  5, -3,  6],
     [-2,  5, -2,  6],
     [ 4, 11, -4,  8]]

L, U = np_descomposicion_LU(A)

print('\nLa descomposición de:')
print(A)
print('es:')
print('L=')
print(L)
print('U=')
print(U)

# Ejemplo 2.
A = [[ 1, 1],
     [-1, 1]]

L, U = np_descomposicion_LU(A)

print('\nLa descomposición de:')
print(A)
print('es:')
print('L=')
print(L)
print('U=')
print(U)

