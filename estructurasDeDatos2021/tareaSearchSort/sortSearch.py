from os import system
from time import sleep

condicion = False
lista = []

def limpiarConsola():
    system("cls")

def sleepScreen(valor):
    sleep(valor)

def appendArray(valor):
    global lista
    lista.append(valor)

def showArray():
    for i in lista:
        print(i)

def insertionSort():
    global lista
    for i in range(1, len(lista)):
        cadena = "["
        for x in lista:
            cadena += str(x) + ", "
        cadena+="]"
        key = lista[i]
        j = i -1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
        print(cadena)
        sleep(1)

def linearSearch(valor):
    global lista
    contadorPosiciones1 = 0
    contadorPosiciones2 = 0
    for i in lista:
        contadorPosiciones2 = 0
        cadena = "["
        for x in lista:
            if contadorPosiciones1 == contadorPosiciones2:
                cadena += "{" + str(x) + "}, "
            else:
                cadena += str(x) + ", "
            contadorPosiciones2 += 1
        cadena+= "] = " + str(valor) + "?"
        print(cadena)
        if i == valor:
            print("Valor encontrado")
            break
        contadorPosiciones1 += 1
        sleep(1)
    if contadorPosiciones1 == len(lista):
        print("No se encontro el valor")
            
        

while (condicion == False):
    limpiarConsola()
    opcion = int(input("Menú\n1.Insertar valores en el array\n2.Imprimir Array\n3.Ordenar Array\n4.Buscar valor en el Array\n5.Salir\nIngrese el número de la opción que desee: "))
    if opcion == 1:
        limpiarConsola()
        appendArray(int(input("Ingrese un valor (numerico) para ingresar en el Array: ")))
    elif opcion == 2:
        limpiarConsola()
        showArray()
        sleepScreen(1)
        input("Pulse enter para continuar")
    elif opcion == 3:
        limpiarConsola()
        insertionSort()
        input("Pulse enter para continuar")
    elif opcion == 4:
        limpiarConsola()
        linearSearch(int(input("Ingrese un valor (numerico) para buscar en el Array: ")))
        input("Pulse enter para continuar")
    elif opcion == 5:
        print("Gracias por utilizar este programa!")
        condicion = True
    else:
        print("Ingrese una opción valida\n\n")
