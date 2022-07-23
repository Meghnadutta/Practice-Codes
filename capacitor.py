# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 22:03:53 2021

@author: Meghna
"""

from math import sin 
from numpy import arange , floor
from pylab import plot,xlabel,ylabel,show 
def f(x,t): 
    return -x**3 + sin(t) 

def f2(v_out,t):
    if(floor((2*t)%2==0)):
        return (1-v_out)/0.01
    else:
        return (-1-v_out)/0.01
a= 0.0 
b = 10.0 
N = 1000
h = (b-a)/N 
tpoints= arange(a,b,h)
xpoints =[]
x=0
for t in tpoints: 
    xpoints.append(x) 
    k1 = h*f2(x,t) 
    k2 = h*f2(x+0.5*k1,t+0.5*h) 
    k3 = h*f2(x+0.5*k2,t+0.5*h) 
    k4 = h*f2(x+k3,t+h) 
    x += (k1+2*k2+2*k3+k4)/6 
plot(tpoints,xpoints) 
xlabel("t") 
ylabel("x(t)") 
show() 