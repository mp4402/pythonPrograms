#Mario Enrique Pisquiy Gómez    Carné 20200399
import numpy as np
from numpy.linalg import inv

A = np.matrix([[2,0,1],
              [3,0,0],
              [5,1,2]])

B = np.matrix([[1,0,1],
              [1,1,0]])

AI = np.matrix([[1,0,0],
               [0,1,0],
               [0,0,1]])

BI = np.matrix([[1,0,0],
               [0,1,0]])

print("Ejercicio 1\n")
print("a) 2(A-2I)^2: \n" + str(2*((A-2*AI)*(A-2*AI))))
print("\n")
print("b) A^t+B^t*B: \n" + str(A.getT()+(B.getT()*B)))
print("\n")
print("c) B*B^t+I: No se puede operar, resulta una matriz de 2*2 y otra de 2*3")
print("\n")

A = np.matrix([[0,1,1],
              [1,0,1],
              [1,1,0]])

AI = np.matrix([[1,0,0],
               [0,1,0],
               [0,0,1]])

print("Ejercicio 2\n")
print("A^2-A-2I: \n" + str((A*A)-A-2*AI))
print("\n")

A = np.matrix([[1,-2,-3],
              [2,2,-3],
              [-3,2,4]])

B = np.matrix([[2,4,6],
              [4,10,12],
              [6,14,18]])

print("Ejercicio 3\n")
print("a) A^-1: \n" + str(inv(A)))
print("b) B^-1: La determinante de la matriz es cero, la matriz no es inversible")
print("\n")

A = np.matrix([[1,1],
              [3,4]])

B = np.matrix([[17,25],
              [2,3]])

Ai = np.matrix([[4,-1],
              [-3,1]])

Bi = np.matrix([[-3,25],
              [2,-17]])

print("Ejercicio 4\n")
print("a) A*B: \n" + str(Ai*Bi))
print("\n")
print("b) A^2*(BA)^-*1B: \n" + str((A*A*A)*(B*B)))
print("\n")
print("c) (A^2)^t: \n" + str(inv((A*A).getT())))
print("\n")
print("d) (A+B)^-1=A^-1+B^-1\n")
print("(A+B)^-1: \n" + str(inv(A+B)))
print("\n")
print("A^-1+B^-1: \n" + str(Ai+Bi))    
print("No es igual (A+B)^-1 que A^-1+B^-1")  