import numpy as np
import sympy as sp
from scipy.linalg import null_space

def encontrarRango(matriz):
    return np.linalg.matrix_rank(np.array(matriz).astype(np.float64))

def encontrarNumeroColumnasFilas(matriz):
    return np.array(matriz).astype(np.float64).shape

def encontrarNulidad(numCols,rango):
    return numCols-rango

def encontrarEspacioNulo(matriz):
    return matriz.nullspace()

def imprimirDatos(key,rango,nulidad,espacioNulo,interpretacion):
    print("El rango de la matriz " + str(key) + " es: "+str(rango))
    print("La nulidad de la matriz " + str(key) + " es: "+str(nulidad))
    print("El espacio nulo de la matriz " + str(key) + " es: \n "+str(espacioNulo))
    print(interpretacion)
    print("\n")

A = sp.Matrix([[1, 0, -1],
               [1, 1, 1],])

B = sp.Matrix([[4, 2],
               [8, 4],
               [0, 0]])

C = sp.Matrix([[1, 1, -1],
               [1, 5, 1],
               [1, -1, -2]])

D = sp.Matrix([[1, 1, 0, 1],
               [0, 1, -1, 1],
               [0, 1, -1, -1]])

E = sp.Matrix([[2, -4, 0, 2, 1],
               [-1, 2, 1, 2, 3],
               [1, -2, 1, 4, 4]])

matrices = [1,2,3,4,5]

for key in matrices:
    print("Matriz " + str(key))
    if key == 1:
        print(A)
        rango = encontrarRango(A)
        forma = encontrarNumeroColumnasFilas(A)
        nulidad = encontrarNulidad(forma[1],rango)
        espacioNulo = encontrarEspacioNulo(A)
        interpretacion = "Esta matriz 2x3, posee 2 variables libre y tan sólo 1 dependiente"
    if key == 2:
        print(B)
        rango = encontrarRango(B)
        forma = encontrarNumeroColumnasFilas(B)
        nulidad = encontrarNulidad(forma[1],rango)
        espacioNulo = encontrarEspacioNulo(B)
        interpretacion = "Esta matriz 3x2 posee 1 variable libre y 1 dependiente"
    if key == 3:
        print(C)
        rango = encontrarRango(C)
        forma = encontrarNumeroColumnasFilas(C)
        nulidad = encontrarNulidad(forma[1],rango)
        espacioNulo = encontrarEspacioNulo(C)
        interpretacion = "Esta matriz 3x3 tiene 2 variables libre y 1 dependinte"
    if key == 4:
        print(D)
        rango = encontrarRango(D)
        forma = encontrarNumeroColumnasFilas(D)
        nulidad = encontrarNulidad(forma[1],rango)
        espacioNulo = encontrarEspacioNulo(D)
        interpretacion = "Esta matriz 3x4 tiene 3 variables libres y 1 dependiente"
    if key == 5:
        print(E)
        rango = encontrarRango(E)
        forma = encontrarNumeroColumnasFilas(E)
        nulidad = encontrarNulidad(forma[1],rango)
        espacioNulo = encontrarEspacioNulo(E)
        interpretacion = "Esta matriz 3x5 tiene 2 variables libre y 3 dependientes"
    imprimirDatos(key,rango,nulidad,espacioNulo,interpretacion)