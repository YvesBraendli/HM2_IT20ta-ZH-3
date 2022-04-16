import numpy as np

def Team12_S8_Aufg3a(x, y):
    Tf = 0
    for i in range(0, x.size-1):
        Tf = Tf + (y[i]+y[i+1])/2 * (x[i+1]-x[i])
    
    return Tf