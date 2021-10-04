# -*- coding: utf-8 -*-
# Solución de sistemas de ecuaciones lineales por Gauss simple.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-09-26
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
2. El ejemplo
    
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


def gauss_simple(A, B):
    '''
        
    ''' 
    m = len(A)
    # Forma aumentada del sistema.
    S = [f[:] for f in A]
    for f in range(m):
        S[f] += [B[f]]
        
    reorganizar_ceros(S)
    # Eliminación hacia adelante.

    def reduccion(M):
        m = len(M)
        S = [f[:] for f in M]  # Copia de la matriz.
        for i in range(1, m):
            for j in range(m+1):
                S[i][j] += -(M[i][0]/M[0][0]) * M[0][j]
        del S[0]
        for i in range(m-1):
            del S[i][0]
        
        return S
    
    R = []
    R += [S[0]]
    for e in range(m-1):
        S = reduccion(S)
        R += [[0]*(e+1) + S[0]]
        if e == m-2:
            break
        pivote_parcial(S)
    # Sustitución hacia atrás.
    sol = [0]*m
    
    for i in range(m):
        sol[m-i-1] += R[m-i-1][m]/R[m-i-1][m-i-1]
        for j in range(i):
            sol[m-i-1] += -sol[m-j-1]*R[m-i-1][m-j-1]/R[m-i-1][m-i-1]

    return sol


# %%Programa principal.

# Matriz de coeficientes constantes.
A = [
     [ 2,  1, -1,  2],
     [ 4,  5, -3,  6],
     [-2,  5, -2,  6],
     [ 4, 11, -4,  8]
                     ]
# Vector de constantes.
B = [5, 9, 4, 2]

# Ejemplo 4.
A4 = [[-1, -1,  6,  9],
      [-5,  5, -3,  6],
      [ 7, -3,  5, -6],
      [ 3, -3, -2,  3]]

B4 = [-29, -54, 38, 41]

A = [[2, 100000],
     [0, -50000]]

B = [100000, -50000] 

# A = [[2, 100000],
#      [1, 1]]

# B = [100000, 2] 

# %%Impresión de resultados.


# Fin del programa.
