# -*- coding: utf-8 -*-
# Descomposición LU para sistemas de ecuaciones lineales.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-09-27
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
2. https://www.youtube.com/watch?v=cApBVYtCwoE
    
'''

# %%Definición de funciones.

def pivote_parcial(M):
    '''
        Pivote parcial de la matriz M. La matriz M debe ser ingresada como una
        lista de listas.
    '''
    m = len(M)      # Tamaño de la matriz.
    lista_max = []  # Separación del espacio de memoria.
    for i in range(m):
        fila = [abs(e) for e in M[i]]  # Copia de la fila con sus absolutos
        lista_max += [fila[0]/max(fila)]  # Máximo valor normalizado fila 1
    
    # Ubicación de la fila del pivote.
    indice = lista_max.index(max(lista_max))
    fila_r = [e for e in M[indice]]  # Copia de fila que se reemplaza.
    del M[indice]  # Se elimina la fila de su ubicación original.
    M.insert(0, fila_r)  # Se ubica la fila en la primera posición.
    # Es una función que no retorna, sino que modifica.


def reorganizar_ceros(S):
    '''
        Función para la verificación de ceros en la diagonal y reorganización.
        S se debe introducir como una lista de listas.
    '''
    m = len(S)

    posible_ubicacion = list(range(0, m))*2
    contador = 0
    while True:
        for i in range(m):
            if S[i][i]==0:
                fila = [e for e in S[i]]  # Copia de la fila con ceros en diag.
                # Se define la nueva ubicación de la fila.
                if (S[i][i]==0) and (S[i+1][i]==0):  # Control de filas seguidas.
                    for j in range(m):
                        if S[i][j] != 0:
                            break
                    ubicacion = j          
                else:
                    ubicacion = posible_ubicacion[i+1]
                del S[i]                   # Se elimina la fila.
                S.insert(ubicacion, fila)  # Nueva ubicación de la fila.
        contador += 1                      # Control de cantidad de ciclos.
        if contador == 2*m:
            break

def matriz_identidad(n):
    '''
        A partir de un orden n dado se crea una matriz identidad como una lista
        de listas.
    '''
    I = []         # Se crea I como una lista vacia.
    # Se ponen unos en la diagonal y ceros en el resto.
    for i in range(n):
        I += [[]]
        for j in range(n):
            if i==j: 
                I[i] += [1]
            else:
                I[i] += [0]
    return I


def descomposicion_LU(A):
    '''
        Descomposición de la Matriz A en las matrices L y U con el método de la
        eliminación de Gauus. La matriz A se debe ingresar como una lista de
        listas.
    '''
    m = len(A)
    L = matriz_identidad(m)  # Se crea L como una matriz identidad.
    U = [f[:] for f in A]    # Se crea U como una copia de A.
    
    for k in range(m):
        U1 = [f[:] for f in U]  # Copia de la matriz.
        eval = list(range(k+1, m))
        for i in eval:
            for j in range(m):
                factor = U[i][k]/U[k][k]
                U1[i][j] += -factor * U[k][j]
                if j==k:
                    L[i][j] = factor            
        U = U1
    
    return L, U


# Matriz de coeficientes constantes.
A = [
     [ 0,  1, -1,  2],
     [ 4,  5, -3,  6],
     [-2,  5, -2,  6],
     [ 4, 11, -4,  8]
                     ]

pivote_parcial(A)     # Reorganiza de acuerdo con la mejor norma.
reorganizar_ceros(A)  # Evita problemas con el cero en la diagonal.

L, U = descomposicion_LU(A)

