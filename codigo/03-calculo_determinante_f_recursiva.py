# -*- coding: utf-8 -*-
# Cálculo del determinante mediante función recursiva
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-09-24
Editor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. https://www.mycompiler.io/view/IVBmA7d
'''


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


# %%Programa principal.

# Ejemplo 1 del determinante
M1 = [[ 2,  1, -1, 2],
      [ 4,  5, -3, 6],
      [-2,  5, -2, 6],
      [ 4, 10, -4, 8]]

# Ejemplo 2 del determinante
M2 = [[ 2,  1,  4, -1],
      [ 3, -2,  1,  0],
      [ 5,  1, -3,  2],
      [-1,  3,  3, -1]]

# Ejemplo 3 del determinante
M3 = [[-9,  7,  2,  5,  7],
      [ 5,  3, -2,  2, -6],
      [ 2, -6, -5, -7, -8],
      [-2,  4, -2, -2, -6]]

# Uso de la función.
det_M1 = determinante(M1)
det_M2 = determinante(M2)
det_M3 = determinante(M3)


# %%Impresión de resultados.

print('\nEl determinante de M1 es:')
print(det_M1)
print('\nEl determinante de M2 es:')
print(det_M2)
print('\nEl determinante de M3 es:')
print(det_M3)

# Fin del programa.
