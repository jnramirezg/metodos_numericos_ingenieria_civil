# -*- coding: utf-8 -*-
# Método de interpolación con la matriz de Vandermonde
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-11-22
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
2. https://es.wikipedia.org/wiki/Matriz_de_Vandermonde
3. https://numpy.org/doc/stable/reference/generated/numpy.vander.html
'''

# %%Importación de librerías.
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# %%Definción de constantes.
x = sp.symbols('x')


# %%Definción de funciones.

def interpolacion_vandermonde(xp, yp):
    '''
        Función que recibe un conjunto de datos xp y un conjunto de datos yp 
        correspondientes a puntos en el plano. Regresa una función f que puede
        ser evaluada y un polinomio interpolador y simbólico. Internamente se
        usa la matriz de Vandermonde.
    '''
    xp = np.array(xp, dtype=float)  # De lista a array.
    yp = np.array(yp, dtype=float)  # De lista a array.
    
    m =len(xp)         # Tamaño del sistema.

    # Matriz de Vandermonde X.
    X = (np.ones((m, m))*xp).T  # Reserva de memoria.    
    for i in range(m):          # Ensamblaje
        X[:, i] = X[:, i]**i

    a = np.linalg.solve(X, yp)  # Obtención de los coeficientes.

    # Polinomio interpolador.
    y = 0                       # Espacio de memoria.
    for i in range(m):
        y += a[i]*x**i

    # Creación de la función interpoladora.
    f = sp.lambdify(x, y)

    return f, y


# %%Ejemplo 1:
# Asignación de puntos.
xp = [0, 2, 3,  4, 5]
yp = [1, 4, 8, 16, 7]

# Evaluación de la función principal.
f, y = interpolacion_vandermonde(xp, yp)

# Impresión del polinomio interpolador
print('\nEl polinomio del ejemplo 1 es:')
print(y)

# Gráfica de resultados
xg = np.linspace(min(xp), max(xp), 100)  # Creación de puntos en x.
yg = f(xg)                               # Evaluación de la función interpola.

fig = plt.figure()
plt.plot(xg, yg, 'r')
plt.plot(xp, yp, 'k.')
plt.show()


# %%Ejemplo 2:
# Asignación de puntos.
xp = [-2, 2]
yp = [ 4, 2]

# Evaluación de la función principal.
f, y = interpolacion_vandermonde(xp, yp)

# Impresión del polinomio interpolador
print('\nEl polinomio del ejemplo 2 es:')
print(y)

# Gráfica de resultados
xg = np.linspace(min(xp), max(xp), 100)  # Creación de puntos en x.
yg = f(xg)                               # Evaluación de la función interpola.

fig = plt.figure()
plt.plot(xg, yg, 'r')
plt.plot(xp, yp, 'k.')
plt.show()


# %%Ejemplo 3:
# Asignación de puntos.
xp = [-15, -12, -10, 0, 3, 3.5, 7, 8]
yp = [  1,   2,   3, 4, 5,   6, 7, 8]

# Evaluación de la función principal.
f, y = interpolacion_vandermonde(xp, yp)

# Impresión del polinomio interpolador
print('\nEl polinomio del ejemplo 3 es:')
print(y)

# Gráfica de resultados
xg = np.linspace(min(xp), max(xp), 100)  # Creación de puntos en x.
yg = f(xg)                               # Evaluación de la función interpola.

fig = plt.figure()
plt.plot(xg, yg, 'r')
plt.plot(xp, yp, 'k.')
plt.show()

# %%Ejemplo 4:
# Asignación de puntos.
xp = [-5, -4, -3, -2, -1, 0, 1, 2, 3,  4,  5]
yp = [25, 16,  9,  4,  1, 0, 1, 4, 9, 16, 25]

# Evaluación de la función principal.
f, y = interpolacion_vandermonde(xp, yp)

# Impresión del polinomio interpolador
print('\nEl polinomio del ejemplo 4 es:')
print(y)

# Gráfica de resultados
xg = np.linspace(min(xp), max(xp), 100)  # Creación de puntos en x.
yg = f(xg)                               # Evaluación de la función interpola.

fig = plt.figure()
plt.plot(xg, yg, 'r')
plt.plot(xp, yp, 'k.')
plt.show()

# Fin del programa.
