# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 09:12:50 2021

@author: Meghna
"""
import numpy as np
import matplotlib.pyplot as plt

def f(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    fx = 10*(y-x)
    fy = 28*x - y - z*x
    fz = x*y- z*(8.0/3.0)
    return (np.array([fx,fy,fz], dtype='double'))

r = np.array([0.0,1.0,0.0],dtype='double')
a=0.0
b= 50.0
n= 10000
h= (b-a)/n
tlist = np.arange(a,b,h)
xlist=[]
ylist=[]
zlist=[]

for t in tlist:
    xlist.append(r[0])
    ylist.append(r[1])
    zlist.append(r[2])
    k_1 = h*f(r, t)
    k_2 = h*f((r+ 0.5*k_1),(t+ 0.5*h))
    k_3 = h*f((r+ 0.5*k_2),(t+ 0.5*h))
    k_4 = h*f((r+k_3),(t+h))
    r = r + ((k_1+ 2*k_2 + 2*k_3 + k_4)/6)
xlist= np.array(xlist)
ylist= np.array(ylist)
zlist= np.array(zlist)


plt.figure(1)
plt.plot(xlist,zlist)
plt.xlabel("x")
plt.ylabel("z")
plt.show()


plt.figure(2)
plt.plot(tlist,ylist,label="y")
plt.xlabel("t")
plt.legend()
plt.show()
#plt.plot(zlist,tlist, label="z")




   
