from metodos import *
import numpy as np
from sympy import *
import csv
import pandas as pd 
x=symbols('x')
y=symbols('y')
f=2*x*y+2*y-x**2-2*y**2
escalonado(f,0.5,0.5)
