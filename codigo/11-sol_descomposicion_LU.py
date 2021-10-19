# -*- coding: utf-8 -*-
# Solución de sistemas de ecuaciones lineales con descomposición LU.
# Con operaciones internas hechas con el módulo numpy.
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

def np_sol_LU(A, B):
    '''
        Función que utiliza el módulo numpy para hallar la solución del sistema
        AX=B, en donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas, sol.
        B: constantes, se ingresa como una lista.
        
        La solución se obtiene con descomposición LU. 
    '''
    L, U = np_descomposicion_LU(A)  # Descomposición LU de A.
    B = np.array([B]).T             # Se convierte B en un np.array de dim adecuada
    m = len(A)                      # Tamaño del sistema.
    
    # Sustitución hacia adelante.
    S1 = np.append(L, B, axis=1)    # Matriz aumentada para el sistema LD=B
    for i in range(m):
        for j in range(i+1, m):
            S1[j, :] = S1[j, :] - S1[i, :]*S1[j, i]
    D = np.array([S1[:, -1]]).T
    
    # Sustitución hacia atrás.
    S2 =  np.append(U, D, axis=1)   # Matriz aumentada para el sistema UX=D
    for i in range(m):
        for j in range(i+1, m):
            p = m-i-1               # Conteo hacia atrás en i.
            q = m-j-1               # Conteo hacia adelante en j.
            S2[q] = S2[q] - S2[p, :]*S2[q, p]/S2[p, p]        
        S2[p, :] =  S2[p, :]/S2[p, p]
    X = S2[:, -1]
    
    return X

# %%Programa principal

# Ejemplo 1.
# Matriz de coeficientes constantes.
A = [[ 1, -2,  1,  3],
     [ 3,  1, -4, -2],
     [ 2,  2, -1, -1],
     [ 1,  4,  2, -5]]
# Vector de constantes.
B = [-3, 7, 1, 12]

X = np_sol_LU(A, B)


# %%Impresión de resultados.
print("La solución del ejemplo 1 es:")
print(X)

# Fin del programa.
