import numpy as np
import sympy as sp

x = np.array([1, 2, 3])         # Vector Fila 1 x 3
print("array x \n " + str(x))
y = np.arange(5)                # Vector Fila 1 x 5 (0 al 4)
print("array y \n " + str(y))
z = np.zeros((2, 3))            # Matriz cero de 2x3
print("array z \n " + str(z))

#Creacion de matrices con numpy
s = np.random.randint(10, size=(5, 5))  #matriz de 5x5 con valores enteros aleatorios con maximo de 10-1
print("matriz s: \n " + str(s))

a = np.array([[1, 2],                    #matriz 3 x 2
               [3, 4],
               [5, 6]])

#suma de matrices
print("matriz a \n " + str(a))
print ("suma a+a \n " + str(a+a))

#producto por un escalar
print("matriz 3*a \n " + str(3*a))
#negativo de una matriz
print("matriz -a  \n " + str(-a))


a = np.array([[1, 0,2, -1]]) # Creacion de matriz con numpy
b= np.array([[1], [0],[2], [-1]])
print("matriz a \n " + str(a))
print("matriz b \n " + str(b))  

#punto elemento a elemento
print("producto elemento a elemento a*a \n " + str(a * a))

print('Producto Punto')
print(np.dot(a,b))


A = np.array([[1, 0,2], [2,3, -1],[4,0,2]])
B = np.array([[1, 0,2], [2,3, -1],[4,0,2]])
C = np.array([[1, 0,2], [2,3, -1],[4,0,2],[1,1,1],[3,6,0]])
D = np.array([[1, 0,2,1,2,5], [2,3, -1,0,0,1],[4,0,2,1,2,4]])

#Producto Matricial
print("producto matricial  AB \n " + str(A*B))


#Forma escalonada
A = sp.Matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 4]])

print("A: \n " + str(A))

print("A Forma escalonada reducida: \n"+ str(A.rref()))