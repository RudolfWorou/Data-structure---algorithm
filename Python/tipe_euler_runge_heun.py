from matplotlib . pyplot import *
from numpy import sqrt , exp , log as ln , sin , cos,linspace, array
from numpy import matrix , zeros
from scipy.integrate.odepack import odeint
#Programme D'Heun pour résoudre les équations différentielles

def Heun(F, t_0 , t_max , N, Y_0) :
    h = ( t_max - t_0) / N
    Y = matrix ( Y_0) ; TY = [ matrix (Y)]
    t = t_0 ; T = [t]
    for n in range (N) :
        Y += h * (F(Y, t)+F(Y+h*F(Y,t),t+h))/2 ; TY. append ( matrix (Y))
        t += h ; T. append (t)
    return (T, TY)
#Programme D'Heun pour résoudre les équations différentielles

def Runge_Kutta(F, t_0 , t_max , N, Y_0) :
    h = ( t_max - t_0) / N
    Y = matrix ( Y_0) ; TY = [ matrix (Y)]
    t = t_0 ; T = [t]
    for n in range (N) :
        k1=h*F(Y,t)
        k2=h*F(Y+k1/2,t+h/2)
        k3=h*F(Y+k2/2,t+h/2)
        k4=h*F(Y+k3,t+h)
        Y += k1/6+k2/3+k3/3+k4/6 ; TY. append ( matrix (Y))
        t += h ; T. append (t)
    return (T, TY)
#Récupération des composantes

def RécupérerComposante(TY, i):
    return [Y[i,0] for Y in TY]
    
#Constante de gravitation universelle
G=1


    
# Problème à deux corps
#Programme D'Euler pour résoudre les équations différentielles

def Euler(F, t_0 , t_max , N, Y_0) :
    h = ( t_max - t_0) / N
    Y = matrix ( Y_0) ; TY = [ matrix (Y)]
    t = t_0 ; T = [t]
    for n in range (N) :
        Y += h * F(Y, t) ; TY. append ( matrix (Y))
        t += h ; T. append (t)
    return (T, TY)
    
#Récupération des composantes

def RécupérerComposante(TY, i):
    return [Y[i,0] for Y in TY]
    


    
# Problème à deux corps

def Pbdeucorps(m1,m2,x1,y1,x2,y2,vx1,vy1,vx2,vy2,to,tmax,N):
# Fonction à utiliser pour Euler dans le cas du problème de deux corps

    def Ft(Y,t):
        xts=Y[0,0]-Y[4,0]
        yts=Y[1,0]-Y[5,0]
        
    #distance à la puissance 3
    
        r=(xts**2+yts**2)**1.5
        Z= matrix([
        [Y[2,0]],[Y[3,0]],
        [-G*m2*xts/r],[-G*m2*yts/r],
        [Y[6,0]],[Y[7,0]],
        [G*m1*xts/r],[G*m1*yts/r]
        ])
        return Z  
#Matrice colonne avec les conditions initiales
    Yo=matrix([
    [x1],[y1],
    [vx1],[vy1],
    [x2],[y2],
    [vx2],[vy2]
    ])
    (T,TY)=Euler(Ft, to , tmax , N, Yo)
    
#Récupération des composantes
    L=[]
    for i in range(0,8):
        L.append(RécupérerComposante(TY, i))
    xs = [] ; ys = [] ; xt = [] ; yt = []
# Centre de gravité des deux masses
    for i in range(len(L[0])):
        xG = (m1*L[0][i] + m2*L[4][i]) / (m1 + m2)
    
        yG = (m1*L[1][i] + m2*L[5][i]) / (m1 + m2)
    
    
        xs.append(L[0][i] - xG)
    
        ys.append(L[1][i] - yG)
    
        xt.append(L[4][i] - xG)
        yt.append(L[5][i] - yG)

#Energie mécanique du système 

    Em=[] # Energie obtenue avec les valeurs du programme d'Euler
    
    
    for i in range(len(L[0])) :
        Em.append(0.5*(m1*(L[2][i]**2+L[3][i]**2)+m2*(L[6][i]**2+L[7][i]**2))-(G*m1*m2/sqrt((L[0][i]-L[4][i])**2+(L[1][i]-L[5][i])**2)))
        
# Energie mécanique réelle
    Emn=[]
    Emn.append((0.5*(m1*(L[2][0]**2+L[3][0]**2)+m2*(L[6][0]**2+L[7][0]**2))-G*m1*m2/((L[0][0]-L[4][0])**2+(L[1][0]-L[5][0])**2)**0.5))
    Emn=Emn*len(Em)
#Représentation des corps et de l'énergie mécanique du système
    grid(True)
    return(xs,ys,xt,yt,T,Em,Emn)

def Pbdecorps(m1,m2,x1,y1,x2,y2,vx1,vy1,vx2,vy2,to,tmax,N):
# Fonction à utiliser pour Runge_kuntta dans le cas du problème de deux corps

    def Ft(Y,t):
        xts=Y[0,0]-Y[4,0]
        yts=Y[1,0]-Y[5,0]
        
    #distance à la puissance 3
    
        r=(xts**2+yts**2)**1.5
        Z= matrix([
        [Y[2,0]],[Y[3,0]],
        [-G*m2*xts/r],[-G*m2*yts/r],
        [Y[6,0]],[Y[7,0]],
        [G*m1*xts/r],[G*m1*yts/r]
        ])
        return Z  
#Matrice colonne avec les conditions initiales
    Yo=matrix([
    [x1],[y1],
    [vx1],[vy1],
    [x2],[y2],
    [vx2],[vy2]
    ])
    (T,TY)=Runge_Kutta(Ft, to , tmax , N, Yo)
    
#Récupération des composantes
    L=[]
    for i in range(0,8):
        L.append(RécupérerComposante(TY, i))
    xs = [] ; ys = [] ; xt = [] ; yt = []
# Centre de gravité des deux masses
    for i in range(len(L[0])):
        xG = (m1*L[0][i] + m2*L[4][i]) / (m1 + m2)
    
        yG = (m1*L[1][i] + m2*L[5][i]) / (m1 + m2)
    
    
        xs.append(L[0][i] - xG)
    
        ys.append(L[1][i] - yG)
    
        xt.append(L[4][i] - xG)
        yt.append(L[5][i] - yG)

#Energie mécanique du système 

    Em=[] # Energie obtenue avec les valeurs du programme d'Euler
    
    
    for i in range(len(L[0])) :
        Em.append(0.5*(m1*(L[2][i]**2+L[3][i]**2)+m2*(L[6][i]**2+L[7][i]**2))-(G*m1*m2/sqrt((L[0][i]-L[4][i])**2+(L[1][i]-L[5][i])**2)))
        
# Energie mécanique réelle
    Emn=[]
    Emn.append((0.5*(m1*(L[2][0]**2+L[3][0]**2)+m2*(L[6][0]**2+L[7][0]**2))-G*m1*m2/((L[0][0]-L[4][0])**2+(L[1][0]-L[5][0])**2)**0.5))
    Emn=Emn*len(Em)
#Représentation des corps et de l'énergie mécanique du système
    grid(True)
    return(xs,ys,xt,yt,T,Em,Emn)
def Pbdeuxcorps(m1,m2,x1,y1,x2,y2,vx1,vy1,vx2,vy2,to,tmax,N):
# Fonction à utiliser pour Heun dans le cas du problème de deux corps

    def Ft(Y,t):
        xts=Y[0,0]-Y[4,0]
        yts=Y[1,0]-Y[5,0]
        
    #distance à la puissance 3
    
        r=(xts**2+yts**2)**1.5
        Z= matrix([
        [Y[2,0]],[Y[3,0]],
        [-G*m2*xts/r],[-G*m2*yts/r],
        [Y[6,0]],[Y[7,0]],
        [G*m1*xts/r],[G*m1*yts/r]
        ])
        return Z  
#Matrice colonne avec les conditions initiales
    Yo=matrix([
    [x1],[y1],
    [vx1],[vy1],
    [x2],[y2],
    [vx2],[vy2]
    ])
    (T,TY)=Heun(Ft, to , tmax , N, Yo)
    
#Récupération des composantes
    L=[]
    for i in range(0,8):
        L.append(RécupérerComposante(TY, i))
    xs = [] ; ys = [] ; xt = [] ; yt = []
# Centre de gravité des deux masses
    for i in range(len(L[0])):
        xG = (m1*L[0][i] + m2*L[4][i]) / (m1 + m2)
    
        yG = (m1*L[1][i] + m2*L[5][i]) / (m1 + m2)
    
    
        xs.append(L[0][i] - xG)
    
        ys.append(L[1][i] - yG)
    
        xt.append(L[4][i] - xG)
        yt.append(L[5][i] - yG)

#Energie mécanique du système 

    Em=[] # Energie obtenue avec les valeurs du programme d'Heun
    
     
    for i in range(len(L[0])) :
        Em.append(0.5*(m1*(L[2][i]**2+L[3][i]**2)+m2*(L[6][i]**2+L[7][i]**2))-(G*m1*m2/sqrt((L[0][i]-L[4][i])**2+(L[1][i]-L[5][i])**2)))
        
# Energie mécanique réelle
    Emn=[]
    Emn.append((0.5*(m1*(L[2][0]**2+L[3][0]**2)+m2*(L[6][0]**2+L[7][0]**2))-G*m1*m2/((L[0][0]-L[4][0])**2+(L[1][0]-L[5][0])**2)**0.5))
    Emn=Emn*len(Em)



    (xa,ya,xb,yb,Ti,Em1,Em2)=Pbdeucorps(m1,m2,x1,y1,x2,y2,vx1,vy1,vx2,vy2,to,tmax,N)
    (xc,yc,xd,yd,Tj,Em3,Em4)=Pbdecorps(m1,m2,x1,y1,x2,y2,vx1,vy1,vx2,vy2,to,tmax,N)
#Représentation des corps et de l'énergie mécanique du système
    grid(True)
    subplot(221)
    scatter([xs[0],xt[0]],[ys[0],yt[0]])
    plot(xs,ys, label="Corps M1_Heun")
    plot(xt,yt, label="Corps M2_Heun")
    legend()
    subplot(222)
    plot(T,Em,label="Energie mécanique avec Heun")
    plot(T,Em1,label="Energie mécanique avec Euler")
    plot(T,Em3,label="Energie mécanique avec Runge_kutta")
    plot(T,Emn, label="Energie mécanique réelle")
    legend()
    subplot(223)
    scatter([xs[0],xt[0]],[ys[0],yt[0]])
    plot(xa,ya, label="Corps M1_Euler")
    plot(xb,yb, label="Corps M2_Euler")
    legend()
    
    subplot(224)
    scatter([xs[0],xt[0]],[ys[0],yt[0]])
    plot(xc,yc, label="Corps M1_Runge_kutta")
    plot(xd,yd, label="Corps M2_Runge_kutta")
    legend()
    show()
    
    
Mo=[
[0.970004,-0.243088,0.466204,0.432366,1.0],
[-0.970004,0.243088,0.466204,0.432366,1.0],
[0.000000,0.000000,-0.932407,-0.864731,1.0]
]    
def adapt(F, t_0 , t_max , Num, Y_0) :
    h = ( t_max - t_0) / Num
    Y=list(Y_0) 
    a=len(Y_0)
    TY =[[[Y_0[i][0]],[Y_0[i][1]],[Y_0[i][2]],[Y_0[i][3]]]for i in range(a)]
    t = t_0 ; T = [t]
    
    for n in range (Num) :
        for i in range(a):
            for j in range(0,4):
                Y[i][j] += h * F(Y, t,i,j) 
                TY[i][j].append(Y[i][j])
            t += h ; T. append (t)
    return (T, TY)    
def Pb_n_corps():
# valeures de test
    S=[5e10,0,0,0,4e9,0,0,0,3e8,0,0,0]
    Yo=matrix([
    [0.0],
    [0.0],
    [0.0],
    [0.0],
    [-1e5],
    [1e3],
    [0.0],
    [3e4],
    [1e7],
    [-1e6],
    [0.0],
    [0.0]
    ])
    t_max=1e3
    to=0.0
   
#Calcul des accélérations de chacun des corps

    def Fncorps(M,t,tn,bn):
        N=list(M)
        n=len(M)
        Fr=[0,0]; Ac=[0,0]; Vx=[]; Vy=[]
        T=[0]
        delta_t=madelta
        mt=0;a=0;b=0
        for j in range(n):
            mt+=M[j][4]
            a+=M[j][0]*M[j][4]
            b+=M[j][1]*M[j][4]
        Xg=[a/mt]; Yg=[b/mt]
    
        xg=0
        yg=0
        for i in range(n):
            for j in range(n):
                if j!=i:
                    r=sqrt((M[i][0]-M[j][0])**2+(M[i][1]-M[j][1])**2)
                    Fr[0]+=G*M[i][4]*M[j][4]*(M[j][0]-M[i][0])/(r**3)
                    Fr[1]+=G*M[i][4]*M[j][4]*(M[j][1]-M[i][1])/(r**3)
                    
            Ac[0]=Fr[0]/M[i][4]
            Ac[1]=Fr[1]/M[i][4]
            N[i][0]=M[i][2]
            N[i][1]=M[i][3]
            N[i][2]=Ac[0]
            N[i][3]=Ac[1]
        return N[tn][bn]
    
# Calcul des différentes trajectoires
    (T,TY)=adapt(Fncorps,0,10,1000,Mo)
#Récupération des composantes
    # L=[]
    # mt=0
    # for k in range(len(S)):
    #     mt+=S[k]
    # for i in range(len(S)):
    #     L.append(RécupérerComposante(TY, i))
    # xG=[]; yG=[]
    # for j in range(len(L[0])):
    # 
    #     xg=0; yg=0
    #    
    #     for k in range(int(len(S)/4)):
    #     
    #         xg+=((S[4*k]*L[4*k][j])/mt)
    #         yg+=((S[4*k]*L[4*(k+1)][j])/mt)
    #     xG.append(xg)
    #     yG.append(yg)
    # for k in range(int(len(S)/4)):
    #     plot(L[4*k]-xG,L[4*(k+1)]-yG,label="corps k")
    return TY   
        
        
#METHODE
def soustraireliste(L,P):
    C=[]
    for i in range(len(L)):
        C.append(L[i]-P[i])
    return C
NOMBRE=100000
M=[
[0.970004,-0.243088,0.0,0.0,1.0],
[-0.970004,0.243088,0.0,0.0,1.0],
[0.000000,0.000000,-1.0,1.0,1.0]
]
madelta=5e-5
def ncorps():
    (n,p)=(len(M),len(M[0]))
# Calcul théorique de l'énergie mécanique
    E=0
    for i in range(n):
        E+=0.5*M[i][4]*(M[i][2]**2+M[i][3]**2)
        
    for i in range(n):
        r=0
        for j in range(i+1,n):
            r=sqrt((M[i][0]-M[j][0])**2+(M[i][1]-M[j][1])**2)
            E-=G*M[i][4]*M[j][4]/r
    
# Instant d'après
    N=list(M)
    Em=0; step=-1; Emeca=[E]; t=0
    Fr=[0,0]; Ac=[0,0]; Vx=[]; Vy=[]
    L=[[[M[i][0]],[M[i][1]],[M[i][2]],[M[i][3]]]for i in range(n)]
    T=[0]
    delta_t=madelta
    mt=0;a=0;b=0
    for j in range(n):
        mt+=M[j][4]
        a+=M[j][0]*M[j][4]
        b+=M[j][1]*M[j][4]
    Xg=[a/mt]; Yg=[b/mt]
    for _ in range(NOMBRE):
        xg=0
        yg=0
        for i in range(n):
            t+=delta_t
            Em+=0.5*M[i][4]*(M[i][2]**2+M[i][3]**2)
            for j in range(n):
                if j!=i:
                    r=sqrt((M[i][0]-M[j][0])**2+(M[i][1]-M[j][1])**2)
                    Fr[0]+=G*M[i][4]*M[j][4]*(M[j][0]-M[i][0])/(r**3)
                    Fr[1]+=G*M[i][4]*M[j][4]*(M[j][1]-M[i][1])/(r**3)
                    if j >i:
                        Em-=G*M[i][4]*M[j][4]/r
                        #accélération
            Ac[0]=Fr[0]/M[i][4]
            Ac[1]=Fr[1]/M[i][4]
            #nouvelles vitesses
            N[i][2]=M[i][2]+delta_t*Ac[0]
            N[i][3]=M[i][3]+delta_t*Ac[1]
            L[i][2].append(N[i][2])
            L[i][3].append(N[i][3])
            #nouvelles accélérations
            N[i][0]=M[i][0]+delta_t*(N[i][2]+M[i][2])/2
            N[i][1]=M[i][1]+delta_t*(N[i][3]+M[i][3])/2
            
            
            M[i][0]=N[i][0]
            M[i][1]=N[i][1]
            M[i][2]=N[i][2]
            M[i][3]=N[i][3]
            
            xg+=(M[i][4]*N[i][0])/mt
            yg+=(M[i][4]*N[i][1])/mt
            
            L[i][0].append(N[i][0])
            L[i][1].append(N[i][1])
            Emeca.append(Em)
            T.append(t)
            Ed=((Em-Emeca[i])/delta_t)/E
        # if Ed >0.000004:
        #     delta_t*=0.0001
        # # if Ed<0.4*0.7:
        # #     delta_t*=1.1
        # if delta_t>madelta:
        #     delta_t=madelta
        # # elif delta_t<madelta/50000:
        # #     delta_t=madelta/50000
                
        Xg.append(xg)
        Yg.append(yg)
        
            
    grid=True
    subplot(121)
    for i in range(n):
        # scatter(L[i][0][0],L[i][1][0])
        #plot(L[i][0],L[i][1])
        scatter([L[i][0][0]-Xg[0]],[L[i][1][0]-Yg[0]])
        plot(soustraireliste(L[i][0],Xg),soustraireliste(L[i][1],Yg), label='Corps '+ str(i+1)) 
        legend()
    subplot(122)
    plot(T,Emeca, label="Energie mécanique")
    plot(T,[Emeca[0]]*len(T),label="Energie réelle")
    legend()
    show()
    
    
def main():
    ncorps()

if __name__=="__main__":
    main()