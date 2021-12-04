# -*- coding: utf-8 -*-
# Método de interpolación trazadores lineales
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-12-04
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
'''

# %%Importación de librerías.
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# %%Definición de funciones

def f(xg, xp, yp):
    x = sp.symbols('x')  # Variable simbólica general.
    n = len(xp)          # Cantidad de puntos.
    pto = np.array([np.array(xp), np.array(yp)]).T  # Conversión a np.array()
    pto = pto[np.lexsort(np.fliplr(pto).T)]         # Ordena de acuerdo con x.
    xp = pto[:, 0]
    yp = pto[:, 1]
    
    mi = (yp[1:]-yp[:-1]) / (xp[1:]-xp[:-1])  # Pendiente
    yi = yp[:-1] + mi*(x-xp[:-1])             # Función simbólica i.
    
    y = 0  # Espacio de memoria para solución.
    
    # Primer intervalo
    f0 = sp.lambdify(x, yi[0])  # Se convierte en función la primera ecuación.
    linf = xp[0]<=xg            # Si es mayor que el primer punto: 1, de  lo contrario 0.
    lsup = xg<=xp[1]            # Si es menor que el segundo punto: 1, de lo contrario 0.
    y += linf*lsup * f0(xg)
    
    # Los otros intervalos
    for i in  range(1, n-1):
        fi = sp.lambdify(x, yi[i])  # Se convierte en función i en ecuación.
        linf = xp[i]<xg             # Si es mayor que el punto i: 1, de  lo contrario 0.
        lsup = xg<=xp[i+1]          # Si es menor que el punto i+1: 1, de lo contrario 0.
        y += linf*lsup * fi(xg)

    return y


# %%Ejemplo 1
# Asignación de puntos.
xp = [4.5, 3.0, 7.0, 9.0]
yp = [1.0, 2.5, 2.5, 0.5]

# Gráfica de resultados
xg = np.linspace(min(xp), max(xp),1000)
yg = f(xg, xp, yp)  # Evaluación de la función principal.

fig = plt.figure()
plt.plot(xg, yg, 'b')
plt.plot(xp, yp, 'k.')
plt.show()

# Fin del programa.

