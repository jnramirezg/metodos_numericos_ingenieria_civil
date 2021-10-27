# -*- coding: utf-8 -*-
# Método iterativo de Jacobi, usando Numpy.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-10-24
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca

1. Khoury R., Harder, D. W. (2016). Numerical Méthods and Modelling for 
Engineering. Springer.

'''
# %%Importación de librerías.
import numpy as np


# %%Definición de funciones.

def np_metodo_jacobi(A, B):
    '''
        Solución de un sistema AX=B, donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas
        B: constantes, se ingresa como una lista.
        Se usa el método iterativo de Jacobi con numpy sin considerar mejoramiento de la
        convergencia.
    '''
    A = np.array(A)
    B = np.array(B)
    n = len(A)       # Tamaño del sistema.
    
    # Se definen las matrices constantes del método.
    D = np.diag(np.diag(A))
    Dinv = np.diag(1/np.diag(A))
    T = A-D
    # Se define X0, para la primera iteración.
    X0 = np.zeros(n)

    toler = 0.0000000000000001
    paso = 0

    while True:
        TX0 = T@X0
        B_TX0 = B-TX0
        X1 = Dinv@B_TX0
        paso += 1
        # Criterio de convergencia
        dis_puntos = sum((X1-X0)**2)**0.5
        if dis_puntos < toler:
            print(f"Se hicieron {paso} iteraciones")
            break
        X0 = X1
        # Criterio de divergencia
        if paso==10000:
            X0 = 'No converge'
            break
    X = X0
    return X


# %%Programa principal.

# Ejemplo 1.
A1 = [[11, -9],
      [11, 13]]

B1 = [99, 286]

sol_1 = np_metodo_jacobi(A1, B1)


# Ejemplo 2.
A2 = [[11, 13],
      [11, -9]]
B2 = [286, 99]

sol_2 = np_metodo_jacobi(A2, B2)


# Ejemplo 3.
A3 = [[  1, -6,  0],
      [ -4,  2,  0],
      [  7,  2,  0]]

B3 = [10, 8, 4]

sol_3 = np_metodo_jacobi(A3, B3)


# Ejemplo 4.
A4 = [[ 1, -1,  1],
      [ 2,  4,  2], 
      [ 1, -1,  1]]

B4 = [1, 2, 1]

sol_4 = np_metodo_jacobi(A4, B4)


# Ejemplo 5.
# La solución es (1.0, -1.0, 1.0)
A5 = [[0,  1, 1],
      [1,  2, 1],
      [2, -1, 1]]

B5 = [0, 0, 4]

sol_5 = np_metodo_jacobi(A5, B5)


# Ejemplo 7.
# Las soluciones son 1/3 y 2/3
A6 = [[0.00000000000000000000000003, 3.0000],[1.0000, 1.0000]]
B6 = [ 2.00000000000000000000000001, 1.0000] 

sol_6 = np_metodo_jacobi(A6, B6)


# Ejemplo 8.
# Las soluciones son 1/3 y 2/3
A7 = [[                      1.0000, 1.0000],
      [0.00000000000000000000000003, 3.0000]]
B7 = [ 1.0000, 2.00000000000000000000000001]

sol_7 = np_metodo_jacobi(A7, B7)


# %%Impresión de resultados.

print('\nLa solución del ejemplo 1 es:')
print(sol_1)
print('\nLa solución del ejemplo 2 es:')
print(sol_2)
print('\nLa solución del ejemplo 3 es:')
print(sol_3)
print('\nLa solución del ejemplo 4 es:')
print(sol_4)
print('\nLa solución del ejemplo 5 es:')
print(sol_5)
print('\nLa solución del ejemplo 7 es:')
print(sol_6)
print('\nLa solución del ejemplo 8 es:')
print(sol_7)


# Fin del programa.
