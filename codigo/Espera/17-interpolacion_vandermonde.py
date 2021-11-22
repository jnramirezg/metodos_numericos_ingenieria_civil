import numpy as np
import sympy as sp


x = sp.symbols('x')
xp = [1, 2, 3, 4]

yp = [1, 4, 9, 16]

def interpolacion_vandermonde(xp, yp):
    '''
        Recibe un conjunto de n puntos (xi, yi) y devuelve una función
        polinómica interpoladora f, que puede ser evaluada. El polinomio
        resultante pasa por todos los puntos y es de grado n-1.
        
        Se requieren los módulos numpy y sympy.
    '''
    xp = np.array(xp)  # De lista a array.
    yp = np.array(yp)  # De lista a array.
    
    m =len(xp)         # Tamaño del sistema.
    
    # Matriz de Vandermonde X.
    X = (np.ones((m, m))*xp).T  # Reserva de memoria.    
    for i in range(m):          # Ensamblaje
        X[:, i] = X[:, i]**i

    a = np.linalg.solve(X, yp)  # Obtención de los coeficientes.

    # Polinomio interpolador.
    y =0                        # Espacio de memoria.
    for i in range(m):
        y += a[i]*x**i
    
    # Creación de la función interpoladora.
    f = sp.lambdify(x, y)

    return f

