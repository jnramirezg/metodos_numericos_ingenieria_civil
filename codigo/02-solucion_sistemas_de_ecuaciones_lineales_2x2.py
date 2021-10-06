# -*- coding: utf-8 -*-
# Solución sistema de ecuaciones lineales 2 x 2
# %%Información
'''
Universidad Nacional de Colombia
Facultad de Ingeniería y Arquitectura
Métodos Numéricos Aplicados a la Ingeniería Civil

Fecha de creación: 2021-09-24
Autor: Juan Nicolás Ramírez Giraldo (jnramirezg@unal.edu.co)

"Cum cogitaveris quot te antecedant, respice quot sequantur" Séneca


Referencias:
1. Chapra, S. C. & Canale, R. P. (2015). Métodos Numéricos para ingenieros 
   (7ª ed.). México D.F.: Mc Graw Hill.
'''


# %% Definción de funciones.

def sol_2x2_mejorado(a, b, c, d, e, f):
    '''
        Solucionador básico de ecuaciones 2x2 a partir de los parámetros 
        a, b, c, d, e, f.
        
        Donde:
        ax + by = c
        dx + ey = f
    '''
    if (a*e - b*d) == 0:
        if (-b*f + c*e) == 0 and (a*f - c*d) == 0:
            solucion = 'Infinitas soluciones'
        else:
            solucion = 'No tiene solución'
    else:     
        x = (-b*f + c*e)/(a*e - b*d)  # Solución de x obtenida a mano.
        y = (a*f - c*d)/(a*e - b*d)   # Solución de y obtenida a mano.
        solucion = (x, y)

    return solucion


# %%Programa principal e impresión  de resultados.

# Ejemplo 1
a, b, c, d, e, f = 3, 2, 18, -1, 2, 2
print('\nEjemplo 1:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Ejemplo 2
a, b, c, d, e, f = -1, 2, 2, -1, 2, 1
print('\nEjemplo 2:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Ejemplo 3
a, b, c, d, e, f = -1, 2, 2, -2, 4, 4
print('\nEjemplo 3:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Ejemplo 4.1
# Si se ponen nueves o ceros se puede obtener cualquiera de los 3 resultados.
a, b, c, d, e, f = -2.499999999999999/5, 1, 1.0000000000000001, -1/2, 1, 1
print('\nEjemplo 4.1:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Ejemplo 4.2
# Agregando un 9
a, b, c, d, e, f = -2.4999999999999999/5, 1, 1.0000000000000001, -1/2, 1, 1
print('\nEjemplo 4.2:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Ejemplo 4.3
# Quitando un cero.
a, b, c, d, e, f = -2.499999999999999/5, 1, 1.000000000000001, -1/2, 1, 1
print('\nEjemplo 4.3:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Ejemplo 4.4
# Quitando dos ceros.
a, b, c, d, e, f = -2.499999999999999/5, 1, 1.00000000000001, -1/2, 1, 1
print('\nEjemplo 4.4:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Ejemplo 4.5
# Agregrando un nueve y quitando un cero.
a, b, c, d, e, f = -2.4999999999999999/5, 1, 1.000000000000001, -1/2, 1, 1
print('\nEjemplo 4.5:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Fin del programa.
