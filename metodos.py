import numpy as np
from sympy import *
def biseccion(fun,a,b,eps):
    print('biseccion:')
    x = symbols('x')
    f=fun
    f_prime = f.diff(x)
    f = lambdify(x, f)
    f_prime = lambdify(x, f_prime)
    dis=b-a
    i=1
    arr=[]
    while not(dis<eps):
        c=(a+b)/2
        fa=f(a)
        fb=f(b)
        fc=f(c)
        f_prim_a=f_prime(a)
        f_prim_c=f_prime(c)
        arr.append([i,round(a,3),round(b,3),round(c,3),round(fa,3),round(fc,3),round(fb,3),round(dis,3)])
        cambia = np.sign(f_prim_a)*np.sign(f_prim_c)
        if cambia <= 0: 
            b = c
        if cambia > 0:
            a = c
        dis = b-a  
        i=i+1 
    print(f'la raiz es {c}')
    return arr

def newton(f,a,eps):
    print('Newton:')
    x = symbols('x')
    f_prime = f.diff(x)
    f_prime2= f_prime.diff(x)
    f_prime = lambdify(x, f_prime)
    f_prime2 = lambdify(x, f_prime2)
    dis=2*eps
    xi=a
    arr=[]
    while (dis>=eps):
        xnuevo=xi-f_prime(xi)/f_prime2(xi)
        dis=abs(xnuevo-xi)
        arr.append([round(xi,3),round(xnuevo,3),round(dis,3)])
        xi=xnuevo
    print(f'la raiz es {xi}')
    return arr

def escalonado(f,i_0,j_0):
    i=i_0
    j=j_0
    print('escalonado:')
    x = symbols('x')
    y = symbols('y')
    a = symbols('a')
    print(i,j)
    fun=lambdify([x,y],f)
    f_prime=(lambdify([x,y],f.diff(x)),lambdify([x,y],f.diff(y)))
    s_0=(f_prime[0](i,j),f_prime[1](i,j))
    g=fun(i+a*s_0[0],j+a*s_0[1])
    g_prim=diff(g,a)
    m=solve(g_prim,a)
    i=i+m[0]*s_0[0]
    j=j+m[0]*s_0[1]
    while i!=0 and j!=0:
        s=(f_prime[0](i,j),f_prime[1](i,j))
        i=s[0]
        j=s[1]
        print(i,j)






