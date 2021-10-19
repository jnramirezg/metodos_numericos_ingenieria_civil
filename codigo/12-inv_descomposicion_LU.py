# -*- coding: utf-8 -*-
# Cálculo de la inversa de una matriz con descomposición LU.
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


def np_inversa_LU(A):
    '''
        Se obtiene la matriz inversa de A a partir de la descomposición LU
        hecha con la función np_descomposicion_LU(). La matriz A se debe
        ingresar como una lista de listas.
        
        Devuelve Ainv como np.array()
    '''
    A = np.array(A, dtype=float)

    L, U = np_descomposicion_LU(A)  # Descomposición LU de A.
    m = len(L)                      # Tamaño del sistema.

    # Eliminación hacia adelante.
    S1 = np.append(L, np.eye(m), axis=1)    # Matriz aumentada de L.
    for i in range(m):
        for j in range(i+1, m):
            S1[j, :] = S1[j, :] - S1[i, :]*S1[j, i]    
    Linv = S1[:, m:] 
    
    # Eliminación hacia atrás.
    S2 = np.append(U, np.eye(m), axis=1)    # Matriz aumentada de U.
    for i in range(m):
        for j in range(i+1, m):
            p = m-i-1               # Conteo hacia atrás en i.
            q = m-j-1               # Conteo hacia adelante en j.
            S2[q] = S2[q] - S2[p, :]*S2[q, p]/S2[p, p]        
        S2[p, :] =  S2[p, :]/S2[p, p]    
    Uinv = S2[:, m:]
    
    Ainv = Uinv@Linv  # A^(-1) = U^(-1)*U^(-1)
    
    return Ainv


# %%Programa principal.

# Ejemplo
A = [[ 1, -2,  1,  3],
     [ 3,  1, -4, -2],
     [ 2,  2, -1, -1],
     [ 1,  4,  2, -5]]

Ainv = np_inversa_LU(A)
verificacion = A @ Ainv - np.eye(4)


# %%Impresión de resulados
print("Dada la matriz A=")
print(A)
print("\nSu matriz inversa es:")
print(Ainv)
print("\nse verifica que A @ Ainv - np.eye(4) = 0")
print(np.isclose(verificacion, 0))
