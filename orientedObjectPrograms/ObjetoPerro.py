class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def incrAge(self) -> None:
        self.edad = self.edad + 1

    def walking(self):
        self.walk = True

Perro1 = Perro("Pooky",8,"Basset Hound")
print(f"Perro 1: \n Nombre: {Perro1.nombre} \n Edad: {Perro1.edad} año(s) \n Raza: {Perro1.raza}")
Perro1.incrAge()
print(f"Perro 1: \n Nombre: {Perro1.nombre} \n Edad: {Perro1.edad} año(s) \n Raza: {Perro1.raza}")