import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

def f1(x):
    return ((funcionesRestrictivas[0][0]*x)-funcionesRestrictivas[0][2])/(funcionesRestrictivas[0][1]*-1)

def f2(x):
    return ((funcionesRestrictivas[1][0]*x)-funcionesRestrictivas[1][2])/(funcionesRestrictivas[1][1]*-1)

def f3(x):
    return ((funcionesRestrictivas[2][0]*x)-funcionesRestrictivas[2][2])/(funcionesRestrictivas[2][1]*-1)

funcionObjetivo = []
funcionObjetivo.append(int(input("Ingrese el valor x1 de la función objetivo: ")))
funcionObjetivo.append(int(input("Ingrese el valor x2 de la función objetivo: ")))
funcionesRestrictivas = [[0 for x in range(3)] for y in range(3)]
funcionesRestrictivas[0][0] = int(input("Ingrese el valor x1 de la función restrictiva 1: "))
funcionesRestrictivas[0][1] = int(input("Ingrese el valor x2 de la función restrictiva 1: "))
funcionesRestrictivas[0][2] = int(input("Ingrese el valor restictivo de la función restrictiva 1: "))
funcionesRestrictivas[1][0] = int(input("Ingrese el valor x1 de la función restrictiva 2: "))
funcionesRestrictivas[1][1] = int(input("Ingrese el valor x2 de la función restrictiva 2: "))
funcionesRestrictivas[1][2] = int(input("Ingrese el valor restictivo de la función restrictiva 2: "))
funcionesRestrictivas[2][0] = int(input("Ingrese el valor x1 de la función restrictiva 3: "))
funcionesRestrictivas[2][1] = int(input("Ingrese el valor x2 de la función restrictiva 3: "))
funcionesRestrictivas[2][2] = int(input("Ingrese el valor restictivo de la función restrictiva 3: "))
posiblesSoluciones = {}
contadorSoluciones = 0
intersecciones = {}
contadorIntersecciones = 0
x = range(-5,50)
x = Symbol('x')                     
x1, =  solve(f1(x)-f2(x))
y1 = f1(x1)
intersecciones[contadorIntersecciones] = [x1,y1]
contadorIntersecciones+=1
x2, =  solve(f1(x)-f3(x))           
y2 = f1(x2)
intersecciones[contadorIntersecciones] = [x2,y2]
contadorIntersecciones+=1
x3, =  solve(f2(x)-f3(x))                                       
y3 = f2(x3)
intersecciones[contadorIntersecciones] = [x3,y3]
contadorIntersecciones+=1
x4 = funcionesRestrictivas[0][2]/funcionesRestrictivas[0][0]
y4 = 0
intersecciones[contadorIntersecciones] = [x4,y4]
contadorIntersecciones+=1
x5 = 0
y5 = funcionesRestrictivas[0][2]/funcionesRestrictivas[0][1]
intersecciones[contadorIntersecciones] = [x5,y5]
contadorIntersecciones+=1
x6 = funcionesRestrictivas[1][2]/funcionesRestrictivas[1][0]
y6 = 0
intersecciones[contadorIntersecciones] = [x6,y6]
contadorIntersecciones+=1
x7 = 0
y7 = funcionesRestrictivas[1][2]/funcionesRestrictivas[1][1]
intersecciones[contadorIntersecciones] = [x7,y7]
contadorIntersecciones+=1
x8 = funcionesRestrictivas[2][2]/funcionesRestrictivas[2][0]
y8 = 0
intersecciones[contadorIntersecciones] = [x8,y8]
contadorIntersecciones+=1
x9 = 0
y9 = funcionesRestrictivas[2][2]/funcionesRestrictivas[2][1]
intersecciones[contadorIntersecciones] = [x9,y9]
contadorRectas = 0
for i in range(contadorIntersecciones):
    contadorRectas=0
    if intersecciones[i][0] >= 0 and intersecciones[i][1] >= 0:
        for j in range(3):
            if ((intersecciones[i][0]*funcionesRestrictivas[j-1][0]) + (intersecciones[i][1]*funcionesRestrictivas[j-1][1])) <= funcionesRestrictivas[j-1][2]:
                contadorRectas+=1
    if contadorRectas == 3:
        posiblesSoluciones[contadorSoluciones] = [intersecciones[i][0],intersecciones[i][1]]
        contadorSoluciones+=1
solucion=[]
solucionNumero =0
for i in range(contadorSoluciones):
    if i == 0:
        solucionNumero = posiblesSoluciones[i][0]*funcionObjetivo[0] + posiblesSoluciones[i][1]*funcionObjetivo[1]
        solucion.append(posiblesSoluciones[i][0])
        solucion.append(posiblesSoluciones[i][1])
    else:
        if (posiblesSoluciones[i][0]*funcionObjetivo[0] + posiblesSoluciones[i][1]*funcionObjetivo[1]) > solucionNumero:
            solucionNumero = posiblesSoluciones[i][0]*funcionObjetivo[0] + posiblesSoluciones[i][1]*funcionObjetivo[1]
            solucion[0] = posiblesSoluciones[i][0]
            solucion[1] = posiblesSoluciones[i][1]

print("La solución es producir " + str(solucion[0]) + " del producto x1 y " + str(solucion[1]) + " del producto x2")