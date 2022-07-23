# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:28:36 2021

@author: Meghna
"""
#numerical differentiation
import numpy as np
import matplotlib.pyplot as plt
"""
f= lambda x: np.sin(x)**2
(x,h) = np.linspace(0,np.pi,1000,retstep=True)
#Z= np.array([2,3,4,5,6,7])
#print(Z[2:],Z[:-2])
dfdh = (f(x[1:])-f(x[:-1]))/h #left and right
dfdh_c= (f(x[2:])-f(x[:-2]))/(2*h) #central method
plt.plot(x[:-1],dfdh)
plt.plot(x,f(x))
plt.plot(x[:-2],dfdh_c)
#plt.legend()
plt.xlim(0,np.pi)
plt.show()
"""
N= 100
(x,h) = np.linspace(0,1,N+1,retstep=True)
print(x,h)
y= x**10

I_rect= h*np.sum(y)
I_trap = h*(np.sum(y[1:-1])+((y[0]+y[-1])/2))

#rectangle(riemannnian integral rule)
print(I_rect,I_rect*11)

#trapezium rule
print(I_trap,I_trap*11)
 
#simpsons 1/3rd rule
simp_onethird_rule= (h*(y[0]+y[-1]+2*np.sum(y[2:-1:2])+4*np.sum(y[1:-1:2]))/3)
print(simp_onethird_rule,simp_onethird_rule*11)
w= np.ones_like(y)
w[1:-1:2]=4
w[2:-1:2]=2
print(y)
print(w)
print(np.dot(y,w)*h/3)