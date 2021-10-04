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

#%% Definición de funciones

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


def gauss_jordan(A, B):
    '''
    
    '''
    m = len(A)
    # Forma aumentada del sistema.
    S = [f[:] for f in A]
    for f in range(m):
        S[f] += [B[f]]
        
    pivote_parcial(S)
    reorganizar_ceros(S)
    
    for k in range(m):
        S1 = [f[:] for f in S]  # Copia de la matriz.
        eval = list(range(m))
        eval.remove(k)
        for i in eval:
            for j in range(m+1):
                if i==j: pass  # ¿Si se necesita este comando?
                S1[i][j] += -(S[i][k]/S[k][k]) * S[k][j]
        # Se normaliza la fila
        S1.insert(k, [0]*(m+1))
        for j in range(m+1):
             S1[k][j] += S1[k+1][j]/S1[k+1][k]
        del S1[k+1]  # Se elimina la fila de su ubicación original.
        S = S1

    sol = []
    for e in range(m):
        sol += [S[e][m]]

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


# %%Impresión de resultados.


# Fin del programa.

