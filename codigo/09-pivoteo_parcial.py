# -*- coding: utf-8 -*-
# Pivoteo parcial con Numpy.
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

def np_pivoteo_parcial(S, j):
    '''
        Función que realiza pivoteo parcial a la matriz S que, debe ser
        ingresada como un np.array. Se debe indicar la posición j en la que 
        se va a realizar el pivoteo.
    '''
    R = S[j:, j:]  # Se extrae la matriz con primer elemento el pivote.
    max_fil = abs(R[:,:-1]).max(axis=1)  # Máximo de cada fila.
    col_j = abs(R[:, 0])                 # Elementos bajo el pivote.
    # Máxima relación. Se pone 1e-14 para evitar división entre cero.
    div = col_j/(max_fil + 1e-14)
    idx = np.where(div == max(div))[0][0] + j  # Ubicación del máximo.
    S1 = np.array([f[:] for f in S])           # Copia de S.
    S[j,  :] = S1[idx, :]  # Se ubica la nueva fila pivote.
    S[idx,:] = S1[  j, :]  # Se intercambia con la posición de la ant.


# %%Programa principal e impresión de resultados.

# Ejemplo de pivoteo parcial 1:
S1 = np.array([[ 0, -2,  0,  3,  4],
               [ 0,  1,  0, -2,  5],
               [ 1,  0, -1,  0, -1],
               [ 0,  4,  2,  0,  3]])

print('\nEl ejemplo 1 original es:')
print(S1)
np_pivoteo_parcial(S1, 0)
print('Y el ejemplo 1 con pivoteo parcial es:')
print(S1)


# Ejemplo de pivoteo parcial 2:
S2 = np.array([[ 1, -2,  0,  3,  4],
               [ 0,  0,  0, -2,  5],
               [ 0,  0, -1,  0, -1],
               [ 0,  4,  2,  0,  3]])

print('\nEl ejemplo 2 original es:')
print(S2)
np_pivoteo_parcial(S2, 1)
print('Y el ejemplo 2 con pivoteo parcial es:')
print(S2)

# Fin del programa.

