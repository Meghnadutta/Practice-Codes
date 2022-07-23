# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 16:05:42 2021

@author: Meghna
"""
import numpy as np
import matplotlib.pyplot as plt
"""
def f1(x,t):
    return -x**3 + np.sin(t)

def f2(v_out,t):
    if(np.floor((2*t)%2==0)):
        return (1-v_out)/0.01
    else:
        return (-1-v_out)/0.01
    
def f(r,t):
    x=r[0]
    y=r[1]
    fx= x*y-x
    w=1
    fy=y-x*y+ np.sin(w*t)**2
    return np.array([fx,fy],float)
        

r = np.array([1.0,1.0],float)
a = 0.0
b = 10.0
n = 10
h= (b-a)/n

tlist= np.arange(a,b,h)
xlist=[]
ylist=[]
#euler method RK1

for t in tlist:
    xlist.append(r[0])
    ylist.append(r[1])
    r = r + h*f(r,t)

#RK2
for t in tlist:
    xlist.append(x)
    k_1 = h*f(x, t)
    k_2 = h*f((x + 0.5*k_1), (t + 0.5*h) )
    x = x+ k_2

#RK4

for t in tlist:
    xlist.append(x)
    k_1 = h*f2(x, t)
    k_2 = h*f2((x+ 0.5*k_1),(t+ 0.5*h))
    k_3 = h*f2((x+ 0.5*k_2),(t+ 0.5*h))
    k_4 = h*f2((x+k_3),(t+h))
    x = x + ((k_1+ 2*k_2 + 2*k_3 + k_4)/6)
   
xlist= np.array(xlist)
ylist= np.array(ylist)
plt.plot(tlist,xlist)
plt.plot(tlist,ylist)
plt.xlabel("t")
plt.ylabel("r")
""" 
#RK4 for multi variable

def f(r,t):
    x=r[0]
    y=r[1]
    fx= x*y-x
    w=1
    fy=y-x*y+ np.sin(w*t)**2
    return np.array([fx,fy],float)
    
r = np.array([1.0,1.0],float)
a=0.0
b=10.0
n=1000
h= (b-a)/n
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
plt.plot(tlist,xlist)
plt.plot(tlist,ylist)
plt.xlabel("t")
plt.ylabel("r")
plt.show()
