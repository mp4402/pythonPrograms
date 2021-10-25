import random
class Persona:
    def __init__(self,nombre,edad,DPI,sexo,peso,altura):
        self.nombre = nombre
        self.edad = edad
        self.DPI = DPI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def CalcularIMC(self):
        IMC = self.peso / ((self.altura) * (self.altura))
        if (IMC > 0 and IMC < 20):
            return -1
        elif (IMC >= 20 and IMC <= 25):
            return 0
        elif (IMC > 25):
            return 1
    
    def esMayorDeEdad(self) -> bool:
        if(self.edad >= 18):
            return True
        else:
            return False
        
    
    def GenerarDPI():
        x = 0
        DPI = ""
        while (x != 13):
            DPI += str(random.randint(0,9))
            x+=1
        return DPI
        
    def comprobarSexo(self):
        if (self.sexo != "H" and self.sexo != "M"):
            self.sexo = "H"

    def descripcion(self):
        return "El nombre es: {}, tiene {} año(s), su sexo es: {}, su altura es {} m, pesa {} kg, su índice de masa corporal es: {}, ¿Es mayor de edad? {}".format(self.nombre, self.edad, self.sexo, self.altura, self.peso, IMC, EstadoEdad)

Persona1 = Persona("Juan Acevedo", 25, Persona.GenerarDPI(),"M",0,0)

Persona1.nombre = input("Ingrese su nombre: ")
Persona1.edad = int(input("Ingrese su edad: "))
Persona1.sexo = input("Ingrese su sexo (H = Hombre, M = Mujer): ")
Persona1.peso = int(input("Ingrese su peso (kg): "))
Persona1.altura = float(input("Ingrese su altura (m): "))
Persona1.comprobarSexo()
IMC = Persona1.CalcularIMC()
EstadoEdad = Persona1.esMayorDeEdad()
print(Persona1.descripcion())