from datetime import datetime
from pyathena import connect
from random import randint
from time import sleep
from os import system
import keyboard
import boto3

def generateData():
    now = datetime.now()
    llamada = {}
    llamada['telefonoLlamada'] = randint(40000000,40010100)
    llamada['tiempoLlamada'] = randint(1,1800)
    llamada['tipoLlamada'] = randint(1,5)
    llamada['fechaLlamada'] = dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(str(llamada['telefonoLlamada']), ", ", str(llamada['tiempoLlamada']), ", ", str(llamada['tipoLlamada']), ", ", str(llamada['fechaLlamada']))


if __name__ == '__main__':
    while True:
        eleccion = input("1. Ingresar valores manualmente\n2. Generar los datos aleatoriamente\n3. Salir\n")
        try:
            if int(eleccion) == 1:
                now = datetime.now()
                llamada = {}
                
                llamada['telefonoLlamada'] = int(input("Ingrese el número de teléfono [40000000-40010100]: "))
                while (llamada['telefonoLlamada'] < 40000000 or llamada['telefonoLlamada'] > 40010100):
                    llamada['telefonoLlamada'] = int(input("Ingrese un número de teléfono valido [40000000-40010100]: "))
                
                llamada['tiempoLlamada'] = int(input("Ingrese el tiempo de la llamada [1-1800]: "))
                while (llamada['tiempoLlamada'] < 1 or llamada['tiempoLlamada'] > 1800):
                    llamada['tiempoLlamada'] = int(input("Ingrese un tiempo de llamada valido [1-1800]: "))

                llamada['tipoLlamada'] = int(input("Ingrese el tipo de llamada [1-5]: "))
                while (llamada['tipoLlamada'] < 1 or llamada['tipoLlamada'] > 5):
                    llamada['tipoLlamada'] = int(input("Ingrese un tipo de llamada valido [1-5]: "))
                
                llamada['fechaLlamada'] = dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

                print(str(llamada['telefonoLlamada']), ", ", str(llamada['tiempoLlamada']), ", ", str(llamada['tipoLlamada']), ", ", str(llamada['fechaLlamada']))
            elif int(eleccion) == 2:
                while True:
                    generateData()
                    sleep(1)
                    if keyboard.is_pressed("q"):
                        break
            elif int(eleccion) == 3:
                break
            else:
                print("Ingrese un valor correcto\n")
        except:
            print("Ingrese un valor correcto\n")