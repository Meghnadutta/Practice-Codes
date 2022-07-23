# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 19:55:18 2022

@author: Meghna
"""

import numpy as np
import matplotlib.pyplot as plt

xy_list = []
circle = []
for i in range(100000):
    x,y = np.random.uniform(-1,1,2)
    xy_list.append((x,y))
    if (x**2 + y**2 <= 1): #the condition given to us
        circle.append((x,y))

circle = np.array(circle)
N = len(xy_list)
C = len(circle)

print("pi value is: ", 4*C/N)
print(100*(np.pi - 4*C/N)/np.pi) #percentage error from pi we calculated
print(100*(np.pi - 22/7)/np.pi) #percentage error from 22/7

xvalues = np.zeros(len(circle))
yvalues = np.zeros(len(circle))

for i in range(len(circle)):
    xvalues[i] = circle[i][0]
    yvalues[i] = circle[i][1]
    
plt.figure(figsize=(10, 10), dpi=80)
plt.scatter(xvalues,yvalues, s = 5,color = "lightpink") #you can change the s value here to change 
                                                        #the size of the scatter points
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Distribution of randomly generated numbers in x^2+y^2<=1")
plt.show()