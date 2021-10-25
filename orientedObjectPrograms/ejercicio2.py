import math
import random
class Persona:
    def __init__(self, Nombre, Edad, dpi):
        self.name = Nombre
        self.age = Edad
        self.DPI = dpi
        self.sexo = "M"
        self.altura = 1.83
        self.peso = 90
    def generarDPI():
        dpi = ""
        i = 0
        while(i != 12):
            dpi += str(random.randrange(0,9))
            i = i + 1
        return dpi

    def CalcularIMC(self):
        respuesta = self.peso/(math.pow(self.altura, 2))
        if respuesta < 20:
            respuesta = -1
        elif respuesta >= 20 and respuesta <= 25:
            respuesta = 0
        else:
            respuesta = 1
        return respuesta
    def Mayorde(self):
        respuesta = False
        if self.age >= 18:
            respuesta = True
        return respuesta
    def comprobarSexo (self, sexoI):
        if self.sexo == sexoI:
            pass
        else:
            self.sexo = "H"
    def toString(self):
        return f"El nombre es: {self.name}, tiene una edad de {self.age}, su DPI es {self.DPI}. Es de sexo {self.sexo}, con una altura de {self.altura} y un peso de {self.peso}\n" 
    def setNombre(self, nuevo):
        self.name = nuevo
    def setEdad(self, nueva):
        self.age = nueva
    def setPeso(self, nuevop):
        self.peso = nuevop
    def setAltura(self, nuevaA):
        self.altura = nuevaA
    def setSexo(self, nuevoS):
        self.sexo = nuevoS
persona = Persona("Carlos", "20", Persona.generarDPI())
print(f"{persona.toString()}")
print("Se comprueba si el peso es ideal")
pesoideal = persona.CalcularIMC()
if pesoideal == -1:
    print("Estas en el peso ideal")
elif pesoideal == 0:
    print("Estas por debajo del peso ideal")
else:
    print("Estas sobre el peso ideal")
print("Vamos a comprobar si el sexo está correcto: \n")
print(f"{persona.sexo}\n")
persona.comprobarSexo("H")
print("Enviamos H para comprobar. Y da como resultado degativo entonces el sexo cambia a H\n")
print(f"{persona.sexo}\n")
print(f"Todos los valores en “human readable” \n")
print(f"{persona.toString()}")
print("-----------------------------------")
print("Se realizan los set de cada atributo")
no = input("Ingrese un nuevo nombre: ")
ag = input("Ingrese una nueva edad: ")
pe = input("Ingrese un nuevo peso: ")
al = input("Ingrese una nueva altura: ")
se = input("Ingrese un nuevo sexo: ")
persona.setNombre(no)
persona.setEdad(ag)
persona.setPeso(pe)
persona.setAltura(al)
persona.setSexo(se)
print(f"Todos los valores en “human readable” con los cambios anteriores: \n")
print(f"{persona.toString()}")
print("Se comprueba si el peso es ideal")
pesoideal = persona.CalcularIMC()
if pesoideal == -1:
    print("Estas en el peso ideal")
elif pesoideal == 0:
    print("Estas por debajo del peso ideal")
else:
    print("Estas sobre el peso ideal")
print("Vamos a comprobar si el sexo está correcto: \n")
print(f"{persona.sexo}\n")
persona.comprobarSexo(persona.sexo)
print("Ahora es correcto entonces no cambia")
print(f"Todos los valores en “human readable” \n")
print(f"{persona.toString()}")