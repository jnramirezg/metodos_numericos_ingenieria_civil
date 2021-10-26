# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 16:07:42 2021

@author: 57312
"""

#%% Importación de librerías.
import numpy as np
import time


# %%Definición de funciones.

def np_gauss_jordan(A, B):
    '''
        Función que utiliza el módulo numpy para hallar la solución del sistema
        AX=B, en donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas, sol.
        B: constantes, se ingresa como una lista.
        La solución se obtiene con la técnica Gauss-Jordan.
        
        Incluye pivoteo parcial y detección de sistemas singulares.
    '''
    A = np.array(A, dtype=float)
    B = np.array([B], dtype=float).T
    
    S = np.append(A, B, axis=1)  # Se crea la matriz aumentada.
    m = S.shape[0]               # Número de filas o de soluciones.
    sol = 0
    
    for j in range(m):
        ### Verificación sistema singular ###
        # Verificación fila.
        fila_j = S[j, :-1]
        ver_ceros_f = np.isclose(fila_j, 0)  # Verificación de ceros.
        sum_ceros_f = ver_ceros_f.sum()      # Cantidad de ceros.      
        # Verificación columna.
        columna_j = S[:, j]
        ver_ceros_c = np.isclose(columna_j, 0)  # Verificación de ceros.
        sum_ceros_c = ver_ceros_c.sum()         # Cantidad de ceros.   

        if sum_ceros_f == m or sum_ceros_c == m :
            sol = 'Sistema singular'
            break
        else:
            ### Pivoteo parcial ###
            R = S[j:, j:]  # Se extrae la matriz con primer elemento el pivote.
            max_fil = abs(R[:,:-1]).max(axis=1)  # Máximo de cada fila.
            col_j = abs(R[:, 0])                 # Elementos bajo el pivote.
            # Máxima relación. Se pone 1e-14 para evitar división entre cero.
            div = col_j/(max_fil + 1e-14)
            idx = np.where(div == max(div))[0][0] + j  # Ubicación del máximo.
            S1 = np.array([f[:] for f in S])           # Copia de S.
            S[j,  :] = S1[idx, :]  # Se ubica la nueva fila pivote.
            S[idx,:] = S1[  j, :]  # Se intercambia con la posición de la ant.

            ### Pivote y normalización ###
            pivote = S[j, j]          # Se define el pivote j, ajj.
            S[j, :] = S[j, :]/pivote  # Normalización con filas fj = (1/ajj)*fj
            for i in range(m):
                if i != j:            # Se exluye la operación cuando i=j.
                    S[i, :] = S[i, :] - S[i, j]*S[j, :]  # Eliminación con fi = fi - (aij)*fj

    if sol != 'Sistema singular':
        sol = list(S[:, -1])  # Se extrae la solución de la última columna de S.
        
    return sol

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

    toler = 0.00000000000000000001
    paso = 0

    while True:
        TX0 = T@X0
        B_TX0 = B-TX0
        X1 = Dinv@B_TX0
        paso += 1
        # Criterio de convergencia
        dis_puntos = sum((X1-X0)**2)**0.5
        if dis_puntos < toler:
            #print(f"Se hicieron {paso} iteraciones")
            break
        X0 = X1
        # Criterio de divergencia
        if paso==100000:
            X0 = 'No converge'
            break
    X = X0
    return X, paso

def np_gauss_seidel(A, B):
    '''
        Solución de un sistema AX=B, donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas
        B: constantes, se ingresa como una lista.
        Se usa el método iterativo de Gauss-Seidel con numpy sin considerar mejoramiento de la
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

    toler = 0.00000000000000000001
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
            #print(f"Se hicieron {paso} iteraciones completas.")
            break

        # Criterio de divergencia
        if paso==100000:
            X0 = 'No converge'
            break
    X = X0
    return X, paso

tiempo_gj = [0, 0, 0, 0, 0, 0, 0, 0]
tiempo_ja = [0, 0, 0, 0, 0, 0, 0, 0]
tiempo_gs = [0, 0, 0, 0, 0, 0, 0, 0]

paso_ja = [0, 0, 0, 0, 0, 0, 0, 0]
paso_gs = [0, 0, 0, 0, 0, 0, 0, 0]
error = 0

m = [10, 50, 100, 500, 1000, 3000,  5000, 10000]
for j in range(3):
    for i in range(len(m)):
        
        while True:
            A = np.random.randint(-10, 10, (m[i], m[i]))/(10*(m[i]+1))
            B = np.random.randint(-10, 10, (m[i]))/(10*(m[i]+1))
            A[np.diag_indices_from(A)]=1
            
            if m[i]<=3000:
                ini_gj = time.time()
                sol_gj = np_gauss_jordan(A, B)
                fin_gj = time.time()
            
            ini_ja = time.time()
            sol_ja, paso_ja_m = np_metodo_jacobi(A, B)
            if sol_ja == 'No converge':
                error += 1
            fin_ja = time.time()
        
            ini_gs = time.time()
            sol_gs, paso_gs_m = np_gauss_seidel(A, B)
            if sol_gs == 'No converge':
               error += 1
            fin_gs = time.time()
            
            if sol_ja != 'No converge' and sol_gs != 'No converge':
                tiempo_gj[i] += fin_gj - ini_gj
                tiempo_ja[i] += fin_ja - ini_ja
                tiempo_gs[i] += fin_gs - ini_gs
                
                paso_ja[i] += paso_ja_m
                paso_gs[i] += paso_gs_m
                break

tiempos = np.array([tiempo_gj, tiempo_ja, tiempo_gs])/3
print(tiempos)
 