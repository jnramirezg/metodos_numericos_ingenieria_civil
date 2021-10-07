# -*- coding: utf-8 -*-
# Solución de sistemas de ecuaciones lineales por la regla de Cramer.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-09-25
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. https://www.mycompiler.io/view/IVBmA7d
2. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
3. Para el ejemplo 4: 
   http://anacrisstina-18.blogspot.com/2013/11/metodo-de-cramer-4x4.html
'''


# %%Importación de librerías.
import numpy as np


# %% Definción de funciones.

def determinante(M):
    '''
        Función recursiva
        Cálculo del determinante de una matriz en forma de lista de listas.
    '''
    if len(M) != len(M[0]):  # Verificación si es cuadrada.
        det = 'La matriz no es cuadrada'
        return det
    det = 0  # Variable de acumulación del determinante.
    if len(M)==2:  # Caso 2x2
        det = M[0][0]*M[1][1] - M[1][0]*M[0][1]
        return det
    else:
        for i in range(len(M)):
            M2 = [f[:] for f in M]  # Se crea una copia
            M2.remove(M[0])
            for j in range(len(M2)):
                M2[j] = M2[j][0:i] + M2[j][i+1:]  # Matriz de cofactores
            det += (-1)**(i)*M[0][i]*determinante(M2)
        return det


def crear_matriz_cuadrada_aleatoria(n):
    '''
        Crear una matriz aleatoria de nxn con valores entre -10 y 10.
    '''
    M =[]               # Reserva de espacio.
    for i in range(n):
        M += [[]]       # Se crea una nueva fila.
        for j in range(n):
            # Se agrega un elemento aleatorio.
            M[i] += [int(np.random.randint(-10, 10))]
    return M


def crear_vector_aleatorio(n):
    '''
        Función para crear un vector de tamaño nx1 con valores entre -5 y 5.
    '''
    B =[]                                          # Reserva de espacio.
    for i in range(n):
        B += [int(np.random.randint(-5, 5))]     # Se agrega un elemento aleatorio.
    return B


def sol_cramer(A, B):
    '''
        Solución de un sistema AX=B, donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas
        B: constantes, se ingresa como una lista.
    '''
    # Se consideran las posibles causas de error.
    if len(A) != len(A[0]):
        sol = 'La matriz de A no es cuadrada.'
    elif len(A) != len(B):
        sol = 'Los tamaños de A y B no coinciden.'
    elif len(A)== 1:
        sol = 'Se debe tener un sistema de mínimo 2x2'
    else:
        det_A = determinante(A)
        if det_A == 0:
            sol = 'Sistema singular'
        else:
            # Cálculos.
            sol = []  # Reserva de espacio de memoria.
            for j in range(len(A)):
                A2 = [f[:] for f in A]  # Se crea una copia.
                for i in range(len(A)):
                    A2[i][j] = B[i]                     
                sol += [determinante(A2)/det_A]
    return sol 


# %%Programa principal.

# Ejemplo 1.
n = 7
A1 = crear_matriz_cuadrada_aleatoria(n)
B1 = crear_vector_aleatorio(n)

# Ejemplo 2.
A2 = [[ 2,  1,  4, -1],
      [ 3, -2,  1,  0],
      [ 5,  1, -3,  2],
      [-1,  3,  3, -1]]

B2 = [1, -1, 4, 3]

# Ejemplo 3.
A3 = [[-9,  7,  2,  5,  7],
      [ 5,  3, -2,  2, -6],
      [ 2, -6, -5, -7, -8],
      [-2,  4, -2, -2, -6]]

B3 = [1, -1, 4, 3]

# Ejemplo 4.
A4 = [[-1, -1,  6,  9],
      [-5,  5, -3,  6],
      [ 7, -3,  5, -6],
      [ 3, -3, -2,  3]]

B4 = [-29, -54, 38, 41]

# Uso de la función principal.
sol_1 = sol_cramer(A1, B1)
sol_2 = sol_cramer(A2, B2)
sol_3 = sol_cramer(A3, B3)
sol_4 = sol_cramer(A4, B4)


# %%Impresión de resultados.

print('\nLa solución del ejemplo 1 es:')
print(sol_1)
print('\nLa solución del ejemplo 2 es:')
print(sol_2)
print('\nLa solución del ejemplo 3 es:')
print(sol_3)
print('\nLa solución del ejemplo 4 es:')
print(sol_4)


# Fin del programa.
