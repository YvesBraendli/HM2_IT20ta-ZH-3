from numpy import cos, pi, zeros

def romberg_extrapolation(f, a, b, m: int):
    m += 1
    T = zeros([m, m])
    for j in range(m):
        h = (b - a) / 2 ** j
        n = (b - a) / h
        T[j, 0] = trapez_integration(f, a, b, int(n))
    for k in range(1, m):
        for i in range(0, (m - k)):
            T[i, k] = (4 ** k * T[i + 1, k - 1] - T[i, k - 1]) / (4 ** k - 1)
    return T

def trapez_integration(f, a, b, n: int):
    area = 0
    h = (b - a) / n
    xi = a
    for i in range(1, n + 1):
        area += (((f(xi) + f(xi + h)) / 2) * h)
        xi = xi + h
    return area

"""
f = Zu integrierende Funktion f(x)
a = Untere Intervallgrenze
b = Obere Intervallgrenze
m = Anzahl Schritte
"""
# Gegeben
f = lambda x: -97000 / (-5 * x ** 2 - 570000)
a = 0
b = 100
m = 4
print(romberg_extrapolation(f, a, b, m))

# Befund (1a)
# [[16.33135257 16.54535787 16.54460532 16.54460732 16.54460732]
#  [16.49185655 16.54465235 16.54460729 16.54460732  0.        ]
#  [16.5314534  16.5446101  16.54460732  0.          0.        ]
#  [16.54132093 16.54460749  0.          0.          0.        ]
#  [16.54378585  0.          0.          0.          0.        ]]

# Schluss
# Das Flugzeug benÃ¶tigt zirka 16.54 Sekunden bis zum Stillstand.

# Befund (1b)
# [[782.25806452 815.83137201 815.6051446  815.60623922 815.60623694]
#  [807.43804513 815.61928381 815.60622212 815.60623695   0.        ]
#  [813.57397414 815.60703848 815.60623672   0.           0.        ]
#  [815.09877239 815.60628683   0.           0.           0.        ]
#  [815.47940822   0.           0.           0.           0.        ]]

# Schluss
# Das Flugzeug benötigt zirka 815.48 m bis zum Stillstand.