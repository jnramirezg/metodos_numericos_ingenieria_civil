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
        if (-b*f + c*e) and (a*f - c*d):
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
print('\nEjemplo 4:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Ejemplo 2
a, b, c, d, e, f = -1, 2, 2, -1, 2, 1
print('\nEjemplo 4:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Ejemplo 3
a, b, c, d, e, f = -1, 2, 2, -2, 4, 4
print('\nEjemplo 4:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Ejemplo 4
# Si se ponen nueves o ceros se puede obtener cualquiera de los 3 resultados.
a, b, c, d, e, f = -2.499999999999999/5, 1, 1.0000000000000001, -1/2, 1, 1
print('\nEjemplo 4:')
print(sol_2x2_mejorado(a, b, c, d, e, f))

# Fin del programa.
