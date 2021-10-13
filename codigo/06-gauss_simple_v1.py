# -*- coding: utf-8 -*-
# Solución de sistemas de ecuaciones lineales por eliminación de Gauss.
# Solución con lista de listas.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-10-12
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
'''


# %% Definción de funciones.

def sol_gauss(A, B):
    '''
        Función que a partir de:
        A: matriz de coeficientes constantes definida como lista de listas.
        B: matriz de constantes definida como una lista.
        
        Devuelve las soluciones del sistema AX=B usando eliminación de Gauss.
    '''
    m = len(A)             # Número de filas de A, cantidad de soluciones.
    S = [f[:] for f in A]  # Se crea S inicialmente como una copia de A.
    
    # Agrego al final de cada fila, el correspondiente elemento de B
    for f in range(m):     
        S[f] += [B[f]]

    ### Eliminación hacia adelante ###    
    for k in range(m-1):
        pivote = S[k][k]  # El elemento de la fila 1, columna 1.
        S1 = [f[:] for f in S]
        for i in range(k+1, m):  # Operaciones: # fi = fi + (-aik/pivote)fk
            factor = -S[i][k]/pivote
            for j in range(k, m+1):
                S1[i][j] = S[i][j] + factor*S[k][j]
        S = S1
    
    ### Sustitución hacia atrás.
    sol = [0]*m  # Se limpia el espacio de memoria de la solución.

    for i in range(1, m+1):
        sol[m-i] +=S[m-i][m] / S[m-i][m-i]
        for j in range(1, i):
            sol[m-i] += -S[m-i][m-j]*sol[m-j]/ S[m-i][m-i]

    return sol


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
sol_1 = sol_gauss(A1, B1)
sol_2 = sol_gauss(A2, B2)
sol_3 = sol_gauss(A3, B3)


# %%Impresión de resultados.

print('\nLa solución del ejemplo 1 es:')
print(sol_1)
print('\nLa solución del ejemplo 2 es:')
print(sol_2)
print('\nLa solución del ejemplo 3 es:')
print(sol_3)

# Fin del programa.
