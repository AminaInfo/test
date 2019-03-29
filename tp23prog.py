import numpy as np
import matplotlib.pyplot as plt 
import scipy.optimize as sp

t,x,y = np.loadtxt('tp23', unpack=True,skiprows=2)

vx=(x[1:]-x[:-1])/(t[1:]-t[:-1])
tv=(t[1:]+t[:-1])/2
X=(x[1:]+x[:-1])/2
ax=(vx[1:]-vx[:-1])/(tv[1:]-tv[:-1])
X1=x[1:-1]


def fonction(X,vx):
    plt.plot(X,vx,'.')
    plt.xlabel("Positions")
    plt.ylabel("Vitesse")
    plt.title("Portrait de phase")
    plt.show()
    
#fonction(X,vx) 

def T1(y,t):
    plt.plot(t,y,'o')
    plt.xlabel("y")
    plt.ylabel("temps")
    plt.title("y en fonction du temps")
    plt.show()
    
def T(x,t):
    plt.plot(t,x,'o')
    plt.xlabel("x")
    plt.ylabel("temps")
    plt.title("x en fonction du temps")
    plt.show()
    
def Y(x,y):
    plt.plot(x,y,'o')
    plt.xlabel("x")
    plt.ylabel("temps")
    plt.title("y en fonction de x")
    plt.show()
    
def acceleration(X1,ax):
    plt.plot(X1,ax,'.')
    plt.xlabel("Positions")
    plt.ylabel("Acceleration")
    plt.title("acceleration en fonction de x")
    plt.show()
    
acceleration(X1,ax)
    
#T1(y,t)
#T(x,t)
#Y(x,y)
