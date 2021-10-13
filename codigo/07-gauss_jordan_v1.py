# -*- coding: utf-8 -*-
# Solución de sistemas de ecuaciones lineales por Gauss simple.
# Lista de listas, pivote parcial y reorganización de ceros.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-10-13
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
    
'''

# %%Importación de librerías


def np_gauss_jordan(A, B):
    '''
        Función que utiliza el módulo numpy para hallar la solución del sistema
        AX=B, en donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas, sol.
        B: constantes, se ingresa como una lista.
        La solución se obtiene con la técnica Gauss-Jordan.
    '''
    import numpy as np  # Esto es por si se olvida llamar antes.
    A = np.array(A)
    B = np.array([B]).T
    
    S = np.append(A, B, axis=1)  # Se crea la matriz aumentada.
    m = S.shape[0]               # Número de filas o de soluciones.

    for j in range(m):
        pivote = S[j, j]          # Se define el pivote j, ajj.
        S[j, :] = S[j, :]/pivote  # Normalización con filas fj = (1/ajj)*fj
        for i in range(m):
            if i != j:            # Se exluye la operación cuando i=j.
                S[i, :] = S[i, :] - S[i, j]*S[j, :]  # Eliminación con fi = fi - (aij)*fj

    sol = S[:, -1]  # Se extrae la solución de la última columna de S.
        
    return list(sol)


# %%Programa principal.

# Ejemplo 1
A1 = [
      [ 2,  1, -1,  2],
      [ 4,  5, -3,  6],
      [-2,  5, -2,  6],
      [ 4, 11, -4,  8]
                      ]

B1 = [5, 9, 4, 2]

# Ejemplo 2.
A2 = [
      [-1, -1,  6,  9],
      [-5,  5, -3,  6],
      [ 7, -3,  5, -6],
      [ 3, -3, -2,  3]
                      ]

B2 = [-29, -54, 38, 41]

# Ejemplo 3.
A3 = [
      [  3, -0.1, -0.2],
      [0.1,    7, -0.3],
      [0.3, -0.2,   10],
                       ]

B3 = [7.85, -19.3, 71.4]

# Uso de la función principal.
sol_1 = np_gauss_jordan(A1, B1)
sol_2 = np_gauss_jordan(A2, B2)
sol_3 = np_gauss_jordan(A3, B3)


# %%Impresión de resultados.

print('\nLa solución del ejemplo 1 es:')
print(sol_1)
print('\nLa solución del ejemplo 2 es:')
print(sol_2)
print('\nLa solución del ejemplo 3 es:')
print(sol_3)

# Fin del programa.
