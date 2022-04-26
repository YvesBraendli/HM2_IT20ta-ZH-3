import os
import numpy as np
from matplotlib import pyplot as plt


def trapetzregel(f, n, a, b, verbose=False):
    f_sum = 0
    h = (b - a) / n
    left_fraction = (f(a) + f(b)) / 2

    for i in range(1, n):
        x = a + i * h
        f_sum += f(x)

    result = h * (left_fraction + f_sum)

    if verbose: print(f"\ta = {a}")
    if verbose: print(f"\tb = {b}")
    if verbose: print(f"\tn = {n}")
    if verbose: print(f"\th = {h}")
    if verbose: print(f"\tTf(h) = {h} * ({left_fraction} + {f_sum}) = {result}\n")

    return result


# Gegeben Aufgabe a
def ai(t):
    return vrel * (µ / (ma - µ * t)) - g


def vi(t):
    return trapetzregel(ai, n, 0, t)


def hi(t):
    return trapetzregel(vi, n, 0, t)


# Gegeben Aufgabe b
def va(t):
    return vrel * np.log(ma / (ma - µ * t)) - g * t


def ha(t):
    return -vrel * (ma - µ * t) / µ * np.log(ma / (ma - µ * t)) + vrel * t - 0.5 * g * t ** 2


if __name__ == "__main__":
    """
    f = Zu integrierende Funktion f(x)
    a = Untere Intervallgrenze
    b = Obere Intervallgrenze
    n = Anzahl Schritte
    """

    # für f(x): vi(t), hi(t), va(t), hi(t) siehe oben unter "Gegeben Aufgabe a"
    # und "Gegeben Aufgabe b"
    a = 0
    b = 190
    n = 190

    # Gegeben Aufgabe a und b
    g = 9.81
    vrel = 2600
    ma = 300000
    me = 80000
    te = 190
    µ = (ma - me) / te

    # Graphische Evaluation
    t = np.linspace(a, b, n)

    # Geschwindigkeit
    plt.plot(t, vi(t), '-.m', label="v(t) per Integral")
    plt.xlabel("t")
    plt.ylabel("v(t)")
    plt.plot(t, va(t), '--b', label="v(t) analytisch")
    plt.xlabel("t")
    plt.legend()
    plt.grid()

    # Graphik anzeigen und speichern
    plt.savefig(os.path.splitext(os.path.basename(__file__))[0] + ".Geschwindigkeit.svg")
    plt.show()

    # Höhe
    plt.plot(t, hi(t), '-.c', label="h(t) per Integral")
    plt.xlabel("t")
    plt.ylabel("h(t)")
    plt.plot(t, ha(t), '--r', label="h(t) analytisch")
    plt.xlabel("t")
    plt.legend()
    plt.grid()

    # Graphik anzeigen und speichern
    plt.savefig(os.path.splitext(os.path.basename(__file__))[0] + ".Höhe.svg")
    plt.show()

    print('Befund:')
    print('Geschwindigkeit |v]:\t%.2f' % vi(te))
    print('Höhe [m]:\t\t\t\t%.2f' % hi(te))
    print('Beschleunigung [g]:\t\t%.2f' % (ai(te) / g))

# Befund:
# Geschwindigkeit |v]:	 1572.71
# Höhe [m]:				79497.49
# Beschleunigung [g]:		2.84