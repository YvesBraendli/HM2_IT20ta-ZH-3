import numpy as np
import matplotlib.pyplot as plt

def Team12_S11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy):
    
    # take x,ymax + hx,y so that the endpoint is included
    x=np.linspace(xmin,xmax,hx)
    y=np.linspace(ymin,ymax,hy)

    # erzeugt eine gatterlinie welche alle x und y punkte enthält
    x,y = np.meshgrid(x,y)
    
    # steigungen bei allen punkten eingesetzt in die differntialgleichung
    
    # damit plt.quiver funktioniert, braucht die funktion für jeden punkt
    # den jeweiligen x und y wert des vektors. für den x wert nehmen wir
    # hier 1 der y wert ergibt sich dann aus der steigungsfunktion, also
    # aus allen errechnet steigungen in slopes. da wir für x 1 nehmen, können
    # wir einfach den ganzen slopes array nehmen für die y werte
    vx=np.ones_like(x)
    vy=f(x,y)
    v=np.sqrt(vx**2+vy**2)
    vx=vx/v
    vy=vy/v
    
    plt.quiver(x,y,vx,vy,color='b',width=0.003,angles='xy')
    plt.show()
    
def f(x,y):
    return x**2 + 0.1*y

xmin = -2
xmax = 2
ymin = -0.5
ymax = 3.5
hx = 25
hy = 25

Team12_S11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy)