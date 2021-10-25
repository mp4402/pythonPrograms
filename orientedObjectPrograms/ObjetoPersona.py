class Persona:
    lugarNacimiento = 'Guatemala'
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

Persona1 = Persona("Juan",18,"5a avenida 13-18 zona 15")
Persona2 = Persona("Miguel", 35, "13 calle 15-21 zona 1")
Persona3 = Persona("Fernanda", 21, "7ma avenida 13-5 zona 2")

print(f"Persona 1: \n Nombre: {Persona1.nombre} \n Edad: {Persona1.edad} \n Dirección: {Persona1.direccion} \n Lugar de nacimiento: {Persona1.lugarNacimiento}\n")
print(f"Persona 2: \n Nombre: {Persona2.nombre} \n Edad: {Persona2.edad} \n Dirección: {Persona2.direccion} \n Lugar de nacimiento: {Persona2.lugarNacimiento}\n")
print(f"Persona 3: \n Nombre: {Persona3.nombre} \n Edad: {Persona3.edad} \n Dirección: {Persona3.direccion} \n Lugar de nacimiento: {Persona3.lugarNacimiento}\n")
