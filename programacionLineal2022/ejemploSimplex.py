#Importación de librerias
from tabulate import tabulate
import pandas as pd
import numpy as np
import time

#Método utilizado para encontrar valores negativos en la fila 0 de la matriz funciones, para determinar el final del algoritmo de simplex
def encontrarNegativos(funciones,indice):
    for i in range(indice):
        if funciones[0,i] < 0:
            return True
    return False

#Método utilizado para encontrar la que será la columna pivote 
def negativoMenor(funciones):
    valorMenor = np.amin(funciones[0])
    indiceValorMenor = np.where(funciones[0] == valorMenor)
    indiceValorMenor = indiceValorMenor[1][0]
    return indiceValorMenor

#Método utilizado para encontrar la que será la fila pivote
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
    
#Método utilizado para encontrar los indices de las filas donde se encuentran las respuestas para los problemas de maximización
def encontrarValoresFinales(funciones,i,funcionObjetivo):
    contadorIndices = 0
    indiceIgual = 0
    indiceSolucion = []
    for x in range(i):
        indice = np.where(funciones[:,x] == 1)
        length = len(indice[0])
        if length == 0:
            indiceSolucion.append(-1)
        else:
            for i in range(len(indiceSolucion)):
                if indiceSolucion[i] == indice[0][0]:
                    indiceIgual = i
                else:
                    contadorIndices+=1
            if contadorIndices == len(indiceSolucion):  
                indiceSolucion.append(indice[0][0])
            else:
                if abs(funcionObjetivo[x]*indice[0][0])>abs(funcionObjetivo[indiceIgual]*indiceSolucion[indiceIgual]):
                    indiceSolucion[indiceIgual] = -1
                    indiceSolucion.append(indice[0][0])
                else:
                    indiceSolucion.append(indice[0][0])
                    
    return indiceSolucion
#Definición de variables
opcion = 0
funcionObjetivo = []
variables = []
condicion = False
#While utilizado para determinar que el usuario ingrese unicamente valores permitidos al programa
while(condicion == False):
    try:
        #Ingreso de datos para el número de variables
        numeroVariables = int(input("Ingrese el número de variables con las que se trabajará: "))
        condicion = True
    except:
        print("Ingrese una opcion valida")

condicion = False
while(condicion == False):
    try:
        #Momento en el que el usuario determina si el problema es de maximización o de minimización 
        opcion = int(input("Elija si el problema es de maximización o de minimización\n1. Maximización\n2. Minimización\n"))
        condicion = True
    except:
        print("Seleccione una opción valida")

#Ciclo utilizado para el ingreso de la función objetivo
for i in range(numeroVariables):
    condicion = False
    while(condicion == False):
        try:
            #Se solicita el nombre de la variable, utilizado principalmente para la impresión de la matriz y el resultado final
            variables.append(str(input("Ingrese el nombre de la variable (texto): ")))
            condicion = True
        except:
            print("Ingrese una opcion valida")
    condicion = False
    while(condicion == False):
        try:
            #Ingreso de los valores de la función objetivo
            funcionObjetivo.append(float(input("Ingrese el valor de la variable " + variables[i] + " de la función objetivo: ")))
            condicion = True
        except:
            print("Ingrese una opcion valida")


condicion = False
while(condicion == False):
    try:
        #Ingreso del número de funciones restrictivas que habrá
        numeroRestrictivas = int(input("Ingrese el número de funciones restrictivas con las que se trabajará: "))
        condicion = True
    except:
        print("Ingrese una opcion valida")

#Creación de la matriz para las funciones restrictivas
funcionesRestrictivas = [[0 for x in range(numeroVariables+2)] for y in range(numeroRestrictivas)]

#Ciclo utilizado para el llenado de la matriz 
for i in range(numeroRestrictivas):
    for j in range(numeroVariables+2):
        if j == numeroVariables+1:
            condicion = False
            while(condicion == False):
                try:
                    #Ingreso de la restricción de la función restrictiva
                    funcionesRestrictivas[i][j] = float(input("Ingrese el valor restrictivo de la función: "))
                    condicion = True
                except:
                    print("Ingrese una opcion valida")
        elif j == numeroVariables:
            condicion = False
            while(condicion == False):
                try:
                    #El usuario elige que signo tiene la función restrictiva
                    funcionesRestrictivas[i][j] = float(input("Ingrese el signo restrictivo de la función\n0. =\n1. >=\n2. <=\n"))
                    #Por el proceso realizado para la minimización, se invierten los signos
                    if opcion == 2:
                        if funcionesRestrictivas[i][j] == 1:
                            funcionesRestrictivas[i][j] = 2
                        elif funcionesRestrictivas[i][j] == 2:
                            funcionesRestrictivas[i][j] = 1 
                    condicion = True
                except:
                    print("Ingrese una opcion valida")
        else:
            condicion = False
            while(condicion == False):
                try:
                    #Ingreso de las valores por variable de la función restricitva
                    funcionesRestrictivas[i][j] = float(input("Ingrese el valor de la variable " + variables[j] + " de la función restrictiva " + str(i+1) + ": "))
                    condicion = True
                except:
                    print("Ingrese una opcion valida")

#Creación de variables, incluyendo la matriz utilizada para el proceso de simplex
funciones = [[0 for x in range(numeroVariables+numeroRestrictivas+3)] for y in range(numeroRestrictivas + 1)]
contadorExceso = 1
contadorHolgura = 1
posicionVariable = 0
contadorCambioColumna = 0

#Ciclo utilizado para el llenado de la matriz
for i in range(numeroRestrictivas+1):
    if i == 0:
        posicionVariable = j-1
        #Ciclo utilizado para el llenado de la primera fila, se ingresa la función objetivo
        for j in range(numeroVariables):
            #El ingreso varía según el tipo de proceso a realizar, es distinto para minimización y maximización
            if opcion == 2:
                funciones[i][j] = (funcionesRestrictivas[j][numeroVariables+1]*-1)
            else:
                funciones[i][j] = (funcionObjetivo[j]*-1)
            funciones[i][posicionVariable] = 1
        funciones[i][numeroVariables+numeroRestrictivas+1] = 0
        variables.append("z")
    else:
        posicionVariable+=1
        #Parte utilizada para el llenado del resto de filas
        for j in range(numeroVariables):
            #De igual forma, aquí se llena diferente según el tipo de proceso a realizar
            if opcion == 2:
                funciones[i][j] = funcionesRestrictivas[j][contadorCambioColumna]
            else:
                funciones[i][j] = funcionesRestrictivas[i-1][j]
        contadorCambioColumna += 1 
        if funcionesRestrictivas[i-1][numeroVariables] == 1:
            funciones[i][posicionVariable] = -1
            variables.append("e"+str(contadorExceso))
            contadorExceso+=1
        elif funcionesRestrictivas[i-1][numeroVariables] == 2:
            funciones[i][posicionVariable] = 1
            variables.append("s"+str(contadorHolgura))
            contadorHolgura+=1
        if opcion == 2:
            funciones[i][numeroVariables+numeroRestrictivas+1] = funcionObjetivo[i-1]
        else:
            funciones[i][numeroVariables+numeroRestrictivas+1] = funcionesRestrictivas[i-1][numeroVariables+1] 

#Se convierte la matriz de un array de arrays a una matriz de numpy
#También se convierte la matriz a un dataframe de pandas, esto para facilitar su impresión en la consola 
variables.append("Valor")
variables.append("Valor")
funciones = np.matrix(funciones)
df = pd.DataFrame(funciones)
print(tabulate(df,headers=variables))

#Proceso de reducción
while(encontrarNegativos(funciones, numeroVariables+numeroRestrictivas) != False):
    #Se halla la columna pivote
    indice = negativoMenor(funciones)
    #Ciclo para dividir los valores en la columna de restricciones según el valor en la columna pivote
    for i in range(numeroRestrictivas+1):
        if funciones[i,indice] == 0:
            funciones[i,numeroVariables+numeroRestrictivas+2] = 0 
        else:
            funciones[i,numeroVariables+numeroRestrictivas+2] = funciones[i,numeroVariables+numeroRestrictivas+1]/funciones[i,indice]
    #Se encuentra el indice de la fila de la fila pivote
    indicePivote = encontrarPivote(funciones,numeroVariables+numeroRestrictivas+2)
    #Encontramos el valor pivote
    valorPivote = funciones[indicePivote,numeroVariables+numeroRestrictivas+2]
    #Se divide toda la fila pivote dentro del valor pivote
    funciones[indicePivote] = funciones[indicePivote]/funciones[indicePivote,indice]
    #Recuperamos el valor pivote
    funciones[indicePivote,numeroVariables+numeroRestrictivas+2]=valorPivote
    
    #Ciclo para reducir las filas para dejar 0s en todas las filas de la columna pivote
    for i in range(numeroRestrictivas+1):
        if i != indicePivote:
            if funciones[i,indice] != 0:
                #Encontramos el valor por el cual multiplicar la fila para reducirla a 0 
                multiplicando = (funciones[i,indice]/funciones[indicePivote,indice])*-1
                #Reducimos la columna a 0
                funciones[i]=funciones[i]+(multiplicando*funciones[indicePivote])
    #Actualizamos el dataframe e imprimimos los resultados
    df = pd.DataFrame(funciones,columns=variables)
    time.sleep(1)
    print("\n")
    print(tabulate(df,headers=variables))

#Inicializamos el array para los valores de la respuesta y el string que exprese la respuesta final
soluciones = []
solucion = "La producción debe ser: "
#Consideramos los métodos que hay y sus diferencias para encontrar la respuesta final
if opcion == 2:
    for i in range(numeroVariables):
        soluciones.append(funciones[0,numeroVariables+1+i])
else:
    indicesSolucion = encontrarValoresFinales(funciones,numeroVariables,funcionObjetivo)
    for i in indicesSolucion:
        if i == -1:
            soluciones.append(0)
        else: 
            soluciones.append(funciones[i,numeroVariables+numeroRestrictivas+1])

#Terminamos de armar el string
for i in range(numeroVariables):
    solucion += str(soluciones[i]) + " unidades de la variable " + variables[i] + " "

#Imprimimos la solución y el máximo / mínimo
print("\n")
print(solucion)
if opcion == 2:
    print("El mínimo es: " + str((funciones[0,numeroVariables+numeroRestrictivas+1])))
else:
    print("El máximo es: " + str((funciones[0,numeroVariables+numeroRestrictivas+1])))