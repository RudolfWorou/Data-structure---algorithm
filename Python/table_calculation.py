from numpy import linspace,exp, matrix, array, cos, sin, pi
from matplotlib.pyplot import grid, axis, scatter, plot, show, legend,Circle
from pylab import *
from cmath import *
import matplotlib.animation as animation
def table(n,p):
    T=linspace(0,2*pi,40)
    X=[cos(t) for t in T]
    Y=[sin(t) for t in T]
    U=[];V=[];A=[];B=[]; C=[];D=[]
    for k in range(0,n+1):
        U.append(exp(2*1j*pi*k/n))
    for k in range(0,n+1):
        V.append((phase(U[k]),k))
    V.sort()
    for k in range(0,n+1):
        A.append(U[V[k][1]])
    Re=[A[i].real for i in range(len(A))]
    Im=[A[i].imag for i in range(len(A))]
    for i in range(0,n+1):
        r=abs(A[i]-A[((i+1)*p)%n])/2
        a=(Re[i]+Re[((i+1)*p)%n])/2
        o=(Im[i]+Im[((i+1)*p)%n])/2
        P=[r*cos(t)+a for t in T]
        M=[r*sin(t)+o for t in T]
       # plot(P,M, 'k', lw=0.1)
        plot([Re[i],Re[((i+1)*p)%n]],[Im[i],Im[((i+1)*p)%n]], 'b--', lw=0.2)
    
    plot(X,Y,'r-')
    plt.axis("equal")
    plt.xlim(-3,3)
    show()


def main():
    table(1000,5)
    table(1000,6)

if __name__=="__main__":
    main()