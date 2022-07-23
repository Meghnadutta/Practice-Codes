# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:25:57 2021

@author: Meghna
"""
import numpy as np
import matplotlib.pyplot as plt
def f(r,t):
    x=r[0]
    y=r[1]
    fx = x-0.5*(x*y)
    fy = 0.5*(x*y) - 2*y
    return(np.array([fx,fy],float))

r = np.array([2.0,2.0],float)
a=0.0
b=30.0
n=100
h=(b-a)/n
tlist = np.arange(a,b,h)
xlist=[]
ylist=[]

for t in tlist:
    xlist.append(r[0])
    ylist.append(r[1])
    k_1 = h*f(r, t)
    k_2 = h*f((r+ 0.5*k_1),(t+ 0.5*h))
    k_3 = h*f((r+ 0.5*k_2),(t+ 0.5*h))
    k_4 = h*f((r+k_3),(t+h))
    r = r + ((k_1+ 2*k_2 + 2*k_3 + k_4)/6)

xlist= np.array(xlist)
ylist= np.array(ylist)
plt.plot(tlist,xlist,label="rabbit population")
plt.plot(tlist,ylist,label = "fox population")
plt.xlabel("t")
plt.ylabel("populations")
plt.legend()