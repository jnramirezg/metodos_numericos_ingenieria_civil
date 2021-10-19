# -*- coding: utf-8 -*-
# Descomposición de Cholesky.
# Con operaciones internas hechas con el módulo numpy.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-10-19
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
    
'''

# %%Importación de librerías.
import numpy as np


# %%Definición de funciones.

def np_desc_cholesky(A):
    '''
        Función que usando el módulo numpy obtiene la descomposición de
        Cholesky de una matriz A cuadrada y simétrica ingresada como una lista
        de listas. 
        
        Se devuelve la matriz L como un np.array().
    '''
    A = np.array(A, dtype=float)    # Se convierte A a un np.array
    m = len(A)
    L = np.zeros((m ,m))
    
    for k in range(m):
        for i in range(k):      
            suma_tem = 0
            suma_tem += A[k, i]
            for j in range(i):
                suma_tem += -(L[i, j]*L[k, j])
            L[k][i] = (suma_tem/L[i, i])
        sum_tem = 0
        sum_tem += A[k, k]
        for j in range(k):
            sum_tem += -(L[k, j])**2
        L[k, k] = (sum_tem**0.5)
    return L


# %%Programa principal.
# Ejemplo 1.
A = [[ 6,   15 , 55],
     [ 15,  55, 225],
     [ 55, 225, 979]]

L = np_desc_cholesky(A)
verificacion = L@L.T


# %%Impresión de resultados.
print("La matriz A=")
print(A)
print("\nAl descomponerse con la técnica de Cholesky, se representa con:")
print(L)
print("\nSe verifica la operación L@L.T")
print(verificacion)

# Fin del programa.