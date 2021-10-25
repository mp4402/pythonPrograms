from flask import Flask
import random

app = Flask(__name__)

def busquedaBinaria(list, searchValue):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if list[mid] < searchValue:
            low = mid + 1
        elif list[mid] > searchValue:
            high = mid - 1
        else:
            return mid
    return -1

@app.route('/linear/<int:numero>/<int:valorBusqueda>', methods=['GET'])
def linearSearch(numero=None, valorBusqueda=None):
    contador = 0
    lista = []
    retorno = "El numero no fue encontrado"
    while (contador <= numero):
        lista.append(random.randint(1,20))
        contador += 1
    lista.sort()
    for n in lista:
        if (n == valorBusqueda):
            retorno = "Número encontrado"
            break
    return f"Lista: {lista} \n Valor para buscar: {valorBusqueda} \n Resultado: {retorno}"

@app.route('/binary/<int:numero>/<int:valorBusqueda>', methods=['GET'])
def binarySearch(numero, valorBusqueda):
    contador = 0
    lista = []
    retorno = "El numero no fue encontrado"
    while (contador <= numero):
        lista.append(random.randint(1,20))
        contador += 1
    lista.sort()
    posicion = busquedaBinaria(lista,valorBusqueda)
    if (posicion != -1):
        retorno = "Numero encontrado"
    return f"Lista: {lista} \n Valor para buscar: {valorBusqueda} \n Resultado: {retorno}"
    

if (__name__ == '__main__'):
    app.run()