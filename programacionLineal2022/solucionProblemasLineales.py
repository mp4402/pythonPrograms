#importación de librerias
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

#definición de funciones para las funciones restrictivas (ya despejadas con respecto a x2 para encontrar las intersecciones)
def f1(x):
    return ((funcionesRestrictivas[0][0]*x)-funcionesRestrictivas[0][2])/(funcionesRestrictivas[0][1]*-1)

def f2(x):
    return ((funcionesRestrictivas[1][0]*x)-funcionesRestrictivas[1][2])/(funcionesRestrictivas[1][1]*-1)

def f3(x):
    return ((funcionesRestrictivas[2][0]*x)-funcionesRestrictivas[2][2])/(funcionesRestrictivas[2][1]*-1)

#ingreso de datos para la función objetivo y las funciones restrictivas
tipo= int(input("Ingrese 1 si es problema de maximización y 2 si es de minimización: "))
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

#Se encuentran las intersecciones, entre las funciones y con los ejes x & y
x = range(-5,50)
x = Symbol('x')
if(funcionesRestrictivas[0][2] > 0 and funcionesRestrictivas[1][2] > 0):              
    x1, =  solve(f1(x)-f2(x))
    y1 = f1(x1)
    intersecciones[contadorIntersecciones] = [x1,y1]
    contadorIntersecciones+=1
if(funcionesRestrictivas[1][2] > 0 and funcionesRestrictivas[2][2] > 0):
    x2, =  solve(f1(x)-f3(x))           
    y2 = f1(x2)
    intersecciones[contadorIntersecciones] = [x2,y2]
    contadorIntersecciones+=1
if(funcionesRestrictivas[1][2] > 0 and funcionesRestrictivas[2][2] > 0):
    x3, =  solve(f2(x)-f3(x))                                       
    y3 = f2(x3)
    intersecciones[contadorIntersecciones] = [x3,y3]
    contadorIntersecciones+=1
if(funcionesRestrictivas[0][0] > 0):
    x4 = funcionesRestrictivas[0][2]/funcionesRestrictivas[0][0]
    y4 = 0
    intersecciones[contadorIntersecciones] = [x4,y4]
    contadorIntersecciones+=1
if(funcionesRestrictivas[0][1] > 0):
    x5 = 0
    y5 = funcionesRestrictivas[0][2]/funcionesRestrictivas[0][1]
    intersecciones[contadorIntersecciones] = [x5,y5]
    contadorIntersecciones+=1
if(funcionesRestrictivas[1][0] > 0):
    x6 = funcionesRestrictivas[1][2]/funcionesRestrictivas[1][0]
    y6 = 0
    intersecciones[contadorIntersecciones] = [x6,y6]
    contadorIntersecciones+=1
if(funcionesRestrictivas[1][1] > 0):
    x7 = 0
    y7 = funcionesRestrictivas[1][2]/funcionesRestrictivas[1][1]
    intersecciones[contadorIntersecciones] = [x7,y7]
    contadorIntersecciones+=1
if(funcionesRestrictivas[2][0] > 0):    
    x8 = funcionesRestrictivas[2][2]/funcionesRestrictivas[2][0]
    y8 = 0
    intersecciones[contadorIntersecciones] = [x8,y8]
    contadorIntersecciones+=1
if(funcionesRestrictivas[2][1] > 0):
    x9 = 0
    y9 = funcionesRestrictivas[2][2]/funcionesRestrictivas[2][1]
    intersecciones[contadorIntersecciones] = [x9,y9]
    contadorRectas = 0

#Se encuentran las intersecciones que sean posibles soluciones
for i in range(contadorIntersecciones):
    contadorRectas=0
    if intersecciones[i][0] >= 0 and intersecciones[i][1] >= 0:
        for j in range(3):
            if(tipo == 1):
                if ((intersecciones[i][0]*funcionesRestrictivas[j-1][0]) + (intersecciones[i][1]*funcionesRestrictivas[j-1][1])) <= funcionesRestrictivas[j-1][2]:
                    contadorRectas+=1
            else:
                if ((intersecciones[i][0]*funcionesRestrictivas[j-1][0]) + (intersecciones[i][1]*funcionesRestrictivas[j-1][1])) >= funcionesRestrictivas[j-1][2]:
                    contadorRectas+=1
    if contadorRectas == 3:
        posiblesSoluciones[contadorSoluciones] = [intersecciones[i][0],intersecciones[i][1]]
        contadorSoluciones+=1
solucion=[]
solucionNumero = 0

#entre las posibles soluciones se encuentra aquella que maximice o minimice la producción
for i in range(contadorSoluciones):
    if i == 0:
        solucionNumero = posiblesSoluciones[i][0]*funcionObjetivo[0] + posiblesSoluciones[i][1]*funcionObjetivo[1]
        solucion.append(posiblesSoluciones[i][0])
        solucion.append(posiblesSoluciones[i][1])
    else:
        if(tipo==1):
            if (posiblesSoluciones[i][0]*funcionObjetivo[0] + posiblesSoluciones[i][1]*funcionObjetivo[1]) > solucionNumero:
                solucionNumero = posiblesSoluciones[i][0]*funcionObjetivo[0] + posiblesSoluciones[i][1]*funcionObjetivo[1]
                solucion[0] = posiblesSoluciones[i][0]
                solucion[1] = posiblesSoluciones[i][1]
        else: 
            if (posiblesSoluciones[i][0]*funcionObjetivo[0] + posiblesSoluciones[i][1]*funcionObjetivo[1]) < solucionNumero:
                solucionNumero = posiblesSoluciones[i][0]*funcionObjetivo[0] + posiblesSoluciones[i][1]*funcionObjetivo[1]
                solucion[0] = posiblesSoluciones[i][0]
                solucion[1] = posiblesSoluciones[i][1]

if contadorSoluciones == 0:
    print("No hay soluciones")
else:
    print("La solución es producir " + str(solucion[0]) + " del producto x1 y " + str(solucion[1]) + " del producto x2")