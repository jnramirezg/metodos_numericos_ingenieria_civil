# -*- coding: utf-8 -*-
# Solución de sistemas de ecuaciones lineales por Gauss-Jordan mejorado.
# Módulo numpy, pivoteo parcial y reorganización de ceros.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-10-17
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
    
'''

# %%Importación de librerías
import numpy as np


# %%Definición de funciones
    
def np_gauss_jordan(A, B):
    '''
        Función que utiliza el módulo numpy para hallar la solución del sistema
        AX=B, en donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas, sol.
        B: constantes, se ingresa como una lista.
        La solución se obtiene con la técnica Gauss-Jordan.
        
        Incluye pivoteo parcial y detección de sistemas singulares.
    '''
    A = np.array(A, dtype=float)
    B = np.array([B], dtype=float).T
    
    S = np.append(A, B, axis=1)  # Se crea la matriz aumentada.
    m = S.shape[0]               # Número de filas o de soluciones.
    sol = 0
    
    for j in range(m):
        ### Verificación sistema singular ###
        # Verificación fila.
        fila_j = S[j, :-1]
        ver_ceros_f = np.isclose(fila_j, 0)  # Verificación de ceros.
        sum_ceros_f = ver_ceros_f.sum()      # Cantidad de ceros.      
        # Verificación columna.
        columna_j = S[:, j]
        ver_ceros_c = np.isclose(columna_j, 0)  # Verificación de ceros.
        sum_ceros_c = ver_ceros_c.sum()         # Cantidad de ceros.   

        if sum_ceros_f == m or sum_ceros_c == m :
            sol = 'Sistema singular'
            break
        else:
            ### Pivoteo parcial ###
            R = S[j:, j:]  # Se extrae la matriz con primer elemento el pivote.
            max_fil = abs(R[:,:-1]).max(axis=1)  # Máximo de cada fila.
            col_j = abs(R[:, 0])                 # Elementos bajo el pivote.
            # Máxima relación. Se pone 1e-14 para evitar división entre cero.
            div = col_j/(max_fil + 1e-14)
            idx = np.where(div == max(div))[0][0] + j  # Ubicación del máximo.
            S1 = np.array([f[:] for f in S])           # Copia de S.
            S[j,  :] = S1[idx, :]  # Se ubica la nueva fila pivote.
            S[idx,:] = S1[  j, :]  # Se intercambia con la posición de la ant.

            ### Pivote y normalización ###
            pivote = S[j, j]          # Se define el pivote j, ajj.
            S[j, :] = S[j, :]/pivote  # Normalización con filas fj = (1/ajj)*fj
            for i in range(m):
                if i != j:            # Se exluye la operación cuando i=j.
                    S[i, :] = S[i, :] - S[i, j]*S[j, :]  # Eliminación con fi = fi - (aij)*fj

    if sol != 'Sistema singular':
        sol = list(S[:, -1])  # Se extrae la solución de la última columna de S.
        
    return sol


# %%Programa principal.

# Ejemplo singular 1:
A1 = [[ 1, -1,  1],
      [ 2,  4,  2], 
      [ 1, -1,  1]]

B1 = [1, 2, 1]

sol_1 = np_gauss_jordan(A1, B1)

# Ejemplo singular 2:
A2 = [[ 1, -1,  1],
      [-2,  2, -2], 
      [ 2,  4,  2]]

B2 = [1, 2, 1]

# Ejemplo singular 3:
sol_2 = np_gauss_jordan(A2, B2)

A3 = [[  1, -6,  0],
      [ -4,  2,  0],
      [  7,  2,  0]]

B3 = [10, 8, 4]

sol_3 = np_gauss_jordan(A3, B3)


# Ejemplo de pivoteo parcial 1:
A4 = [[ 1, -2,  1,  3],
      [ 3,  1, -4, -2],
      [ 2,  2, -1, -1],
      [ 1,  4,  2, -5]]

B4 = [-3, 7, 1, 12]

sol_4 = np_gauss_jordan(A4, B4)


# Ejemplo de pivoteo parcial 2:
A5 = [[ 0, -2,  0,  3],
      [ 0,  1,  0, -2],
      [ 1,  0, -1,  0],
      [ 0,  4,  2,  0]]

B5 = [-3, 1, 1, 2]

sol_5 = np_gauss_jordan(A5, B5)

# %%Impresión de resultados.

print('\nLa solución del ejemplo singular 1 es:')
print(sol_1)
print('\nLa solución del ejemplo singular 2 es:')
print(sol_2)
print('\nLa solución del ejemplo singular 3 es:')
print(sol_3)
print('\nLa solución del ejemplo pivoteo parcial 1 es:')
print(sol_4)
print('\nLa solución del ejemplo pivoteo parcial 2 es:')
print(sol_5)

# Fin del programa.
