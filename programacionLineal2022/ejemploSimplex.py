from tabulate import tabulate
import pandas as pd
import numpy as np

def encontrarNegativos(funciones, i):
    contadorNegativos = False
    if np.any(funciones[0] < 0) == True:
        contadorNegativos = True
    return contadorNegativos

def negativoMenor(funciones):
    valorMenor = np.amin(funciones[0])
    indiceValorMenor = np.where(funciones[0] == valorMenor)
    indiceValorMenor = indiceValorMenor[1][0]
    return indiceValorMenor

funcionObjetivo = []
variables = []
numeroVariables = int(input("Ingrese el número de variables con las que se trabajará: "))

for i in range(numeroVariables):
    variables.append(str(input("Ingrese el nombre de la variable (texto): ")))
    funcionObjetivo.append(int(input("Ingrese el valor de la variable " + variables[i] + " de la función objetivo: ")))

numeroRestrictivas = int(input("Ingrese el número de funciones restrictivas con las que se trabajará: "))
funcionesRestrictivas = [[0 for x in range(numeroVariables+2)] for y in range(numeroRestrictivas)]

for i in range(numeroRestrictivas):
    for j in range(numeroVariables+2):
        if j == numeroVariables+1:
            funcionesRestrictivas[i][j] = int(input("Ingrese el valor restrictivo de la función: "))
        elif j == numeroVariables:
            funcionesRestrictivas[i][j] = int(input("Ingrese el signo restrictivo de la función\n0. =\n1. >=\n2. <=\n"))
        else:
            funcionesRestrictivas[i][j] = int(input("Ingrese el valor de la variable " + variables[j] + " de la función: "))

funciones = [[0 for x in range(numeroVariables+numeroRestrictivas+3)] for y in range(numeroRestrictivas + 1)]

posicionVariable = 0
for i in range(numeroRestrictivas+1):
    if i == 0:
        posicionVariable = j-1
        for j in range(numeroVariables):
            funciones[i][j] = (funcionObjetivo[j]*-1)
        funciones[i][posicionVariable] = 1
        funciones[i][numeroVariables+numeroRestrictivas+1] = 0
    else:
        posicionVariable+=1
        for j in range(numeroVariables):
            funciones[i][j] = funcionesRestrictivas[i-1][j]
        if funcionesRestrictivas[i-1][numeroVariables] == 1:
            funciones[i][posicionVariable] = -1
        else:
            funciones[i][posicionVariable] = 1
        funciones[i][numeroVariables+numeroRestrictivas+1] = funcionesRestrictivas[i-1][numeroVariables+1]

funciones = np.matrix(funciones)
print(funciones)


while(encontrarNegativos(funciones,numeroVariables) != False):
    indice = negativoMenor(funciones)
    for i in range(numeroRestrictivas+1):
        if funciones[i,indice] = 0:
            funciones[i,numeroVariables+numeroRestrictivas+2] = 0 
        else:
            funciones[i,numeroVariables+numeroRestrictivas+2] = funciones[i,numeroVariables+numeroRestrictivas+1]/funciones[i,indice]
    print(funciones)
    
    