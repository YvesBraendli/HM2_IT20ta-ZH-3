# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:51:20 2022

@author: yvesb
"""

import numpy as np
import matplotlib.pyplot as plt

# aufgabe 3a
x = np.array([1981,1984,1989,1993,1997,2000,2001,2003,2004,2010])
y = np.array([0.5,8.2,15.,22.9,36.6,51.,56.3,61.8,65.,76.7])
z = np.polyfit(x,y,9)

def f(x):
    return np.polyval(z,x)

x_values = np.arange(1975,2020,0.1)

plt.plot(x_values,f(x_values),label='polyfit')
plt.plot(x,y,'bo')
plt.grid()
plt.ylim(-100,250)
# Das Polynom ist nicht 100%ig exakt, der zweite Datenpunkt
# wird nicht genau im Zentrum geschnitten.

# aufgabe 3b
x_middleValue = x-x.mean()
z_middleValue = np.polyfit(x_middleValue,y,9)

def f_middleValue(x2):
    return np.polyval(z_middleValue,x2-x.mean())

plt.plot(x_values,f_middleValue(x_values),label='polyfit_middleValue')
plt.plot(x,y,'bo')
plt.grid()
plt.ylim(-100,250)
'''
Die Kurven stimmen nicht mehr überein. Die Kurve mit den verschobenen Werten
bricht an den Enden stark aus und stimmt nur im Mittelteil kurzzeitig mit
dem Polynom der Originaldaten überein.
'''


# aufgabe 3c
print('Schätzwert für 2020:', f_middleValue(2020))

'''
Der Schätzwert liegt bei -257'066.377', dieser liegt im negativen
Bereich, was nicht möglich ist, da es nicht eine negative Anzahl
Haushalte mit einem Computer geben kann.
Somit können solche Polynome nicht für Schätzwerte ausserhalb des Intervalls
der vorhandenen Daten benutzt werden.
'''

# aufgabe 3c
def lagrange(n,i,x_int,x):
    result = 1
    for j in range(0, n):
        if j != i:
            result *= (x_int-x[j])/(x[i]-x[j])
    return result
def lagrange_int(x,y,x_int):
    if len(x) != len(y):
        return 'x and y vectors need to have the same length!'
    result = 0
    for i in range(0, len(x)):
        result += y[i]*lagrange(len(x),i,x_int,x)
    return result
def lagrange_int_vec(x,y,x_int_vec):
    result = np.zeros(len(x_int_vec))
    for i in range(0,len(x_int_vec)):
        result[i] = lagrange_int(x,y,x_int_vec[i])
    return result

y_values_lagrange = lagrange_int_vec(x, y, x_values)
plt.plot(x_values,y_values_lagrange,label='lagrange')
plt.legend()
plt.show()

'''
Diese stimmt mit dem Polynom aus der Aufgabe b überein.
'''