#Mario Enrique Pisquiy Gómez
#Carné 20200399

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

def f1(x):
    return (2*x)-10

def f2(x):
    return 6-x

def f3(x):
    return x+6

plt.figure(1)
x = range(-5,20)
plt.title('Graficas de las funciones de la tarea 3')
plt.plot(x, [f1(i) for i in x])
plt.plot(x, [f2(i) for i in x])
plt.plot(x, [f3(i) for i in x])

plt.xlim(-5, 20)                    
plt.ylim(0, 25)                     
x = Symbol('x')                     
x1, =  solve(f1(x)-f2(x))           
x2, =  solve(f1(x)-f3(x))           
x3, =  solve(f2(x)-f3(x))           

y1 = f1(x1)                         
y2 = f1(x2)                         
y3 = f2(x3)                         

print(str(x1)+","+str(y1))          
print(str(x2)+","+str(y2))          
print(str(x3)+","+str(y3))      
                    
plt.plot(x1,y1,'go',markersize=10)  
plt.plot(x2,y2,'go',markersize=10)  
plt.plot(x3,y3,'go',markersize=10)  

plt.title('Grafica de la region entre las tres rectas')  
plt.fill([x1,x2,x3],[y1,y2,y3],'red',alpha=0.5) 

plt.grid()                          
plt.savefig("grafica.png")          
plt.show()                          