# -*- coding: utf-8 -*-
# Método iterativo de Jacobi, con lista de listas.
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-10-21
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca

1. Khoury R., Harder, D. W. (2016). Numerical Méthods and Modelling for 
Engineering. Springer.

'''
# %%Definición de funciones.

def matriz_D(A):
    '''
        Función a la que se le ingresa una matriz definida como una lista
        de listas, y devuelve una matriz del mismo tamaño, pero únicamente
        con los elementos de la diagonal.
    '''
    n = len(A)     # El número de filas de A.
    m = len(A[0])  # El número de columnas de A.

    # Se crea una matriz de ceros de tamaño n.
    # Se supone que m=n, pero para evitar controlar errores en este paso
    # se crea de manera general.
    D = []
    for i in range(n):
        D += [[]]
        for j in range(m):
            D[i] += [0]

    for i in range(n):      # Recorre n filas.
        for j in range(m):  # Recorre m columnas.
            if i==j:        # Condición 1.
                D[i][j] = A[i][j]
            #else:           # Condición 2.
            #    D[i][j] = 0
    return D


def matriz_T(A):
    '''
        Función a la que se le ingresa una matriz definida como una lista
        de listas, y devuelve una matriz del mismo tamaño y con los mismos
        elementos, pero sin los elementos de la diagonal.
    '''
    n = len(A)     # El número de filas de A.
    m = len(A[0])  # El número de columnas de A.

    # Se crea una matriz de ceros de tamaño n.
    # Se supone que m=n, pero para evitar controlar errores en este paso
    # se crea de manera general.
    T = []
    for i in range(n):
        T += [[]]
        for j in range(m):
            T[i] += [0]

    for i in range(n):      # Recorre n filas.
        for j in range(m):  # Recorre m columnas.
            if i!=j:        # Condición 1, ÚNICO CAMBIO: en vez de ==, !=.
                T[i][j] = A[i][j]
            #else:           # Condición 2.
            #    T[i][j] = 0
    return T

def matriz_ceros(m, n):
    '''
        Se crea una matriz de ceros de tamaño mxn definida 
        como una lista de listas.
    '''
    C = []
    for i in range(n):
        C += [[]]
        for j in range(m):
            C[i] += [0]
    return C

def matriz_Dinv(D):
    '''
        Función que se le ingresa una matriz definida como una lista de litas, 
        y retorna la matriz inversa de la matriz diagonal correspondiente.
    '''
    n = len(D)     # El número de filas de D.
    m = len(D[0])  # El número de columnas de D.
    
    # Se crea el espacio de memoria adecuado con ceros.
    Dinv = matriz_ceros(m, n) # Esta función debe estar en el mismo programa que la función prin.

    for i in range(n):      # Recorre n filas.
        for j in range(m):  # Recorre m columnas.
            if i==j:        # Condición ÚNICA.
                Dinv[i][j] = 1/D[i][j]
    return Dinv

def Mmul_vector(A, B):
    '''
        Función que realiza la multiplicación de una matriz A cuadrada de orden 
        n definida como una lista de listas con un vector B de tamaño n 
        definido como una lista.
        
        Devuelve Mmul, del mismo tamaño que B.
    '''
    n = len(B)                    # Tamaño
    Mmul = matriz_ceros(n, 1)[0]  # Vector de ceros de tamaño n.
    
    for i in range(n):
        for j in range(n):
            Mmul[i] += B[j]*A[i][j]
            
    return Mmul

def Mres_vector(M, N):
    '''
        Función que resta dos vectores M y N definidos como listas, 
        devulve un vector del mismo tamaño con la resta M-N.
    '''
    n = len(M)                    # Tamaño
    Mres = matriz_ceros(n, 1)[0]  # Vector de ceros de tamaño n.
    
    for i in range(n):
        Mres[i] = M[i]-N[i]

    return Mres  

def dis_punto(M, N):
    '''
        Función que devuelve la distancia entre dos puntos definidos como dos
        vectores dentro de listas. Devuelve un escalar.
    '''
    n = len(M)  # Tamaño del vector.
    dist_2 = 0  # Espacio de memoria.
    for i in range(n):
        dist_2 += (M[i]-N[i])**2
    dist = (dist_2)**0.5

    return dist

def metodo_jacobi(A, B):
    '''
        Solución de un sistema AX=B, donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas
        B: constantes, se ingresa como una lista.
        Se usa el método iterativo de Jacobi sin considerar mejoramiento de la
        convergencia.
    '''
    n = len(A)
    # Se definen las matrices constantes del método.
    Dinv = matriz_Dinv(A)
    T = matriz_T(A)

    # Se define X0, para la primera iteración.
    X0 = matriz_ceros(n, 1)[0]

    toler = 0.0000000000000001
    paso = 0

    while True:
        TX0 = Mmul_vector(T, X0)
        B_TX0 = Mres_vector(B, TX0)
        X1 = Mmul_vector(Dinv, B_TX0)
        paso += 1
        if dis_punto(X1, X0) < toler:
            print(f"Se hicieron {paso} iteraciones")
            break
        X0 = X1
        # Criterio de divergencia
        if paso==1000:
            X0 = 'No converge'
            break  
    X = X0
    return X


# %%Programa principal.

# Ejemplo 1:
A1 = [[ 3, -1, -1],
      [-1,  3,  1],
      [ 2,  1,  4]]
B1 = [1, 3, 7]

# Ejemplo 2:
A2 = [[11, -9],[11, 13]]
B2 = [99, 286]

# Ejemplo 2:
A3 = [[11, 13],[11, -9]]
B3 = [286,99]


# %%Impresión de resultados.
print('\nLa solución del ejemplo 1 es:')
sol_1 = metodo_jacobi(A1, B1)
print(sol_1)
print('\nLa solución del ejemplo 2 es:')
sol_2 = metodo_jacobi(A2, B2)
print(sol_2)
print('\nLa solución del ejemplo 3 es:')
sol_3 = metodo_jacobi(A3, B3)
print(sol_3)


# Fin del programa.
