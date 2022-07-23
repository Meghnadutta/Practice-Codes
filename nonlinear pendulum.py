# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:47:30 2021

@author: Meghna
"""

import numpy as np
import matplotlib.pyplot as plt

def f(r,t):
    g = 9.81
    l = 0.1
    theta = r[0]
    w = r[1]
    f_theta = w
    f_w = -(g/l)*np.sin(theta)
    return(np.array([f_theta,f_w], float))

r = np.array([np.pi/180, 0.0],float) 
a = 0
b = 20
n = 100000
h = (b-a)/n
tlist = np.arange(a,b,h)
theta_list=[]
w_list=[]

for t in tlist:
    theta_list.append(r[0])
    w_list.append(r[1])
    k_1 = h*f(r, t)
    k_2 = h*f((r+ 0.5*k_1),(t+ 0.5*h))
    k_3 = h*f((r+ 0.5*k_2),(t+ 0.5*h))
    k_4 = h*f((r+k_3),(t+h))
    r = r + ((k_1+ 2*k_2 + 2*k_3 + k_4)/6)
    
theta_list = np.array(theta_list)
w_list = np.array(w_list)

plt.figure(1)
plt.plot(tlist,theta_list, label = "Theta vs time")
#plt.title("Theta vs time")
plt.plot(tlist,w_list, label= "omega vs time")
plt.legend()
plt.xlabel("time")
plt.show()

plt.figure(2)
plt.plot(tlist,theta_list)
plt.title("theta vs time")
plt.xlabel("time")
plt.ylabel("theta")
plt.show()

plt.figure(3)
plt.plot(w_list,theta_list)
plt.title("theta vs omega")
plt.show()
plt.xlabel("omega")
plt.ylabel("theta")
