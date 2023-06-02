from metodos import *
import numpy as np
from sympy import *
import csv
import pandas as pd 
x=symbols('x')
f=(-0.25*x**4)+(50*x**2)+30*x-1
a=0
b=100
eps=0.04
k=0.001
n=9
bis=(biseccion(f,a,b,eps))
with open('biseccion.csv','w',newline='') as archivo:
    writer=csv.writer(archivo)
    writer.writerow(['i','a','b','c','f(a)','f(c)','f(b)','dis'])
    writer.writerows(bis)
   
csv_table = pd.read_csv("biseccion.csv")
print(csv_table.to_latex(index=False))
print('----------------')
new=newton(f,n,k)
with open('newton.csv','w',newline='') as archivo:
    writer=csv.writer(archivo)
    writer.writerow(['xi','xnuevo','dis'])
    writer.writerows(new)
csv_table = pd.read_csv("newton.csv")
print(csv_table.to_latex(index=False))
s = csv_table.style.highlight_max(axis=None,props='cellcolor:{red}; bfseries: ;')
print(s.to_latex())

