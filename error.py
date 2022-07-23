# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:44:39 2022

@author: Meghna
"""
import numpy as np
import matplotlib.pyplot as plt

def f1(x,t):
    return(-x**3 + x**2)

def f(x,t):
    return (-3*x**2 + 2*x)
    
def euler(a,b,h):  
    x = np.array(1.0,float)
    tlist = np.arange(a,b,h)
    xlist=[]
    #euler method
    for t in tlist:
        xlist.append(x)
        x = x + h*f(x,t)
    return(x)

# i need the absolute value
# i need the calculated value
# i need the difference between these two for different step sizes
# i need to plot the error vs step size graph 

def error(x,t,a,b,h):
    error_value = np.abs(euler(a,b,h) - f1(x,t))
    return(error_value)

error_value = error(1,5,1,5,0.1)
'''    
#rk4    
for t in tlist:
    xlist.append(x)
    
    k_1 = h*f(x, t)
    k_2 = h*f((x+ 0.5*k_1),(t+ 0.5*h))
    k_3 = h*f((x+ 0.5*k_2),(t+ 0.5*h))
    k_4 = h*f((x+k_3),(t+h))
    x = x + ((k_1+ 2*k_2 + 2*k_3 + k_4)/6)
xlist= np.array(xlist)
plt.plot(tlist,xlist)
plt.xlabel("t")
plt.ylabel("x")
plt.show()
'''
