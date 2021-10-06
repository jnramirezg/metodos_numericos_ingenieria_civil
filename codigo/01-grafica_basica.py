# -*- coding: utf-8 -*-
# Grafica básica
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-06-10
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca
'''

# %%Importación de librerías.

import matplotlib.pyplot as plt
import numpy as np


# %%Programa principal

x = np.array([0, 10])  # Definición de puntos de evaluación.
y1 = (18 - 3*x)/2      # Ecuación 1.
y2 = (2 + 1*x)/2       # Ecuación 2.

# Gráfica
plt.figure()                    # Las gráficas siempre inician con este comando
plt.plot(x, y1, label="ec. 1")  # Grafica la primera recta
plt.plot(x, y2, label="ec. 2")  # Grafica la segunda recta
plt.legend()                    # Muestra leyendas
plt.grid()                      # Muestra grilla
plt.show()                      # Imprime la gráfica


# Fin del programa.
