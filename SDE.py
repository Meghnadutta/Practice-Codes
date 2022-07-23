# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:18:46 2022

@author: Meghna
"""

import numpy as np
import matplotlib.pyplot as plt

mu, sigma, x0 = 1,1,2
#T = 1
N = 10**5
dt = 1.0/N
t = np.arange(dt,1+dt, dt)

np.random.seed(2)
dB = np.sqrt(dt)*np.random.randn(N)
B = np.cumsum(dB)
x_theory = x0*np.exp((mu - 0.5*sigma**2)*t + (sigma*B))

#or x_simulation can be a list also. depends on what you need from your code
x_simulation , x = np.zeros(N) , x0

for j in range(N):
    x = mu*x*dt  + sigma*x*dB[j] + x
    x_simulation[j] = x
    
plt.plot(t, x_theory, label = "exact")
plt.plot(t, x_simulation, label = "euler-maruyama")
plt.legend()
plt.grid()