# -*- coding: utf-8 -*-
# Costo computacional del cálculo de determinantes mediante el teorema de 
# Laplace
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-09-25
Editor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. https://www.mycompiler.io/view/IVBmA7d
'''


# %%Importación de librerías.
import matplotlib.pyplot as plt
import numpy as np
import time


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


# %%Programa principal.

tiempos = []  # Espacio para almacenar el tiempo de cálculo.

# Se evalúa el tiempo de cálculo del determinante entre n=2 y n=10.
for i in range(2, 11):
    M = crear_matriz_cuadrada_aleatoria(i)  # Función de creación de matriz.
    inicio = time.time()                    # Tiempo de incio.
    determinante(M)                         # F.del determinante de matrices.
    fin = time.time()                       # Tiempo de fin.
    tiempos += [fin-inicio]

# %%Gráficas.

# Gráfica de costo computacional.
plt.figure()
plt.plot(list(range(2, 11)), tiempos)
plt.xlabel('Tamaño n de la matriz')    # Título del eje x.
plt.ylabel('Tiempo de cálculo [seg]')  # Título del eje y.
plt.show()                             # Imprime la gráfica.

# Fin del programa.
