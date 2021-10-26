# -*- coding: utf-8 -*-
# Método de Gauss-Seidel con Numpy, sin considerar mejoramiento de la solución.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-10-25
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
    
'''

# %%Importación de librerías.
import numpy as np


# %%Definición de funciones.

def np_gauss_seidel(A, B):
    '''
        Solución de un sistema AX=B, donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas
        B: constantes, se ingresa como una lista.
        Se usa el método iterativo de Gauss-Seidel con numpy sin considerar
        mejoramiento de la convergencia.
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
        X = np.array([X0[f] for f in range(n)])
        for i in range(n):
            x_i = Dinv[i, i]*(B[i] - T[i, :]@X0)  
            X0[i] = x_i
        paso += 1
        # Criterio de convergencia
        dis_puntos = sum((X0-X)**2)**0.5
        if dis_puntos < toler:
            print(f"Se hicieron {paso} iteraciones completas.")
            break

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

# Ejemplo 2.
# Las soluciones son 1/3 y 2/3
A2 = [[                      1.0000, 1.0000],
      [0.00000000000000000000000003, 3.0000]]
B2 = [ 1.0000, 2.00000000000000000000000001]


# %%Impresión de resultados.

print('\nLa solución del ejemplo 1 es:')
sol_1 = np_gauss_seidel(A1, B1)
print(sol_1)
print('\nLa solución del ejemplo 2 es:')
sol_2 = np_gauss_seidel(A2, B2)
print(sol_2)

# Fin del programa.
