from matplotlib.cbook import index_of
from tabulate import tabulate
import pandas as pd
import numpy as np
import time

def encontrarNegativos(funciones):
    contadorNegativos = False
    if np.any(funciones[0] < 0) == True:
        contadorNegativos = True
    return contadorNegativos

def negativoMenor(funciones):
    valorMenor = np.amin(funciones[0])
    indiceValorMenor = np.where(funciones[0] == valorMenor)
    indiceValorMenor = indiceValorMenor[1][0]
    return indiceValorMenor

def encontrarPivote(funciones,indice):
    posiblesPivote = funciones[:,indice]
    posiblesPivote[0] = 0
    boolArr = posiblesPivote > 0
    newArr = posiblesPivote[boolArr]
    newArr = posiblesPivote[posiblesPivote > 0]
    pivote = np.amin(newArr)
    indicePivote = np.where(funciones[:,indice] == pivote)
    indicePivote = indicePivote[0][0]
    return indicePivote

def encontrarValoresFinales(funciones,i):
    indiceSolucion = []
    for x in range(i):
        indice = np.where(funciones[:,x] == 1)
        if not indice[0]:
            indiceSolucion.append(-1)
        else:
            indiceSolucion.append(indice[0][0])
    return indiceSolucion

opcion = 0
funcionObjetivo = []
variables = []
condicion = False
while(condicion == False):
    try:
        numeroVariables = int(input("Ingrese el número de variables con las que se trabajará: "))
        condicion = True
    except:
        print("Ingrese una opcion valida")

condicion = False
while(condicion == False):
    try:
        opcion = int(input("Elija si el problema es de maximización o de minimización\n1. Minimización\n2. Maximización\n"))
        condicion = True
    except:
        print("Seleccione una opción valida")

for i in range(numeroVariables):
    condicion = False
    while(condicion == False):
        try:
            variables.append(str(input("Ingrese el nombre de la variable (texto): ")))
            condicion = True
        except:
            print("Ingrese una opcion valida")
    condicion = False
    while(condicion == False):
        try:
            funcionObjetivo.append(float(input("Ingrese el valor de la variable " + variables[i] + " de la función objetivo: ")))
            condicion = True
        except:
            print("Ingrese una opcion valida")
    
condicion = False
while(condicion == False):
    try:
        numeroRestrictivas = int(input("Ingrese el número de funciones restrictivas con las que se trabajará: "))
        condicion = True
    except:
        print("Ingrese una opcion valida")

funcionesRestrictivas = [[0 for x in range(numeroVariables+2)] for y in range(numeroRestrictivas)]

for i in range(numeroRestrictivas):
    for j in range(numeroVariables+2):
        if j == numeroVariables+1:
            condicion = False
            while(condicion == False):
                try:
                    funcionesRestrictivas[i][j] = float(input("Ingrese el valor restrictivo de la función: "))
                    condicion = True
                except:
                    print("Ingrese una opcion valida")
        elif j == numeroVariables:
            condicion = False
            while(condicion == False):
                try:
                    funcionesRestrictivas[i][j] = float(input("Ingrese el signo restrictivo de la función\n0. =\n1. >=\n2. <=\n"))
                    condicion = True
                except:
                    print("Ingrese una opcion valida")
        else:
            condicion = False
            while(condicion == False):
                try:
                    funcionesRestrictivas[i][j] = float(input("Ingrese el valor de la variable " + variables[j] + " de la función restrictiva " + str(i+1) + " : "))
                    condicion = True
                except:
                    print("Ingrese una opcion valida")

funciones = [[0 for x in range(numeroVariables+numeroRestrictivas+3)] for y in range(numeroRestrictivas + 1)]
contadorExceso = 1
contadorHolgura = 1
posicionVariable = 0
for i in range(numeroRestrictivas+1):
    if i == 0:
        posicionVariable = j-1
        for j in range(numeroVariables):
            if opcion == 1:
                funciones[i][j] = funcionObjetivo[j]
            else:
                funciones[i][j] = (funcionObjetivo[j]*-1)
        funciones[i][posicionVariable] = 1
        funciones[i][numeroVariables+numeroRestrictivas+1] = 0
        variables.append("z")
    else:
        posicionVariable+=1
        for j in range(numeroVariables):
            funciones[i][j] = funcionesRestrictivas[i-1][j]
        if funcionesRestrictivas[i-1][numeroVariables] == 1:
            funciones[i][posicionVariable] = -1
            variables.append("s"+str(contadorExceso))
            contadorExceso+=1
        else:
            funciones[i][posicionVariable] = 1
            variables.append("e"+str(contadorHolgura))
            contadorHolgura+=1
        funciones[i][numeroVariables+numeroRestrictivas+1] = funcionesRestrictivas[i-1][numeroVariables+1]
variables.append("Valor")
variables.append("Valor")
funciones = np.matrix(funciones)
df = pd.DataFrame(funciones)
print(tabulate(df,headers=variables))

while(encontrarNegativos(funciones) != False):
    indice = negativoMenor(funciones)
    for i in range(numeroRestrictivas+1):
        if funciones[i,indice] == 0:
            funciones[i,numeroVariables+numeroRestrictivas+2] = 0 
        else:
            funciones[i,numeroVariables+numeroRestrictivas+2] = funciones[i,numeroVariables+numeroRestrictivas+1]/funciones[i,indice]
    indicePivote = encontrarPivote(funciones,numeroVariables+numeroRestrictivas+2)
    valorPivote = funciones[indicePivote,numeroVariables+numeroRestrictivas+2]
    funciones[indicePivote] = funciones[indicePivote]/funciones[indicePivote,indice]
    funciones[indicePivote,numeroVariables+numeroRestrictivas+2]=valorPivote
    for i in range(numeroRestrictivas+1):
        if i != indicePivote:
            if funciones[i,indice] != 0:
                multiplicando = (funciones[i,indice]/funciones[indicePivote,indice])*-1
                funciones[i]=funciones[i]+(multiplicando*funciones[indicePivote])
    df = pd.DataFrame(funciones,columns=variables)
    time.sleep(1)
    print("\n")
    print(tabulate(df,headers=variables))

indicesSolucion = encontrarValoresFinales(funciones,numeroVariables)
soluciones = []
solucion = "La producción debe ser: "
for i in indicesSolucion:
    if i == -1:
        soluciones.append(0)
    else: 
        soluciones.append(funciones[i,numeroVariables+numeroRestrictivas+1])
for i in range(numeroVariables):
    solucion += str(soluciones[i]) + " unidades de la variable " + variables[i] + " "
print(solucion)
if opcion == 1:
    print("El mínimo es: " + str((funciones[0,numeroVariables+numeroRestrictivas+1]*-1)))
else:
    print("El máximo es: " + str((funciones[0,numeroVariables+numeroRestrictivas+1])))