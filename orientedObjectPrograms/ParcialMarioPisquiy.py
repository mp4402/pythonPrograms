import math
class Punto:
    def __init__ (self,puntoX,puntoY):
        self.puntoX = puntoX
        self.puntoY = puntoY

    def __str__(self):
        return f"({self.puntoX},{self.puntoY})"

    def cuadrante(self):
        if (self.puntoX == 0 and self.puntoY != 0):
            return f"El punto ({self.puntoX},{self.puntoY}) esta situado en el eje Y"
        elif (self.puntoX != 0 and self.puntoY == 0):
            return f"El punto ({self.puntoX},{self.puntoY}) esta situado en el eje X"
        elif (self.puntoX == 0 and self.puntoY == 0):
            return f"El punto ({self.puntoX},{self.puntoY}) esta situado en el origen"
        elif (self.puntoX > 0 and self.puntoY > 0):
            return f"El punto ({self.puntoX},{self.puntoY}) esta situado en el cuadrante I"
        elif (self.puntoX < 0 and self.puntoY > 0):
            return f"El punto ({self.puntoX},{self.puntoY}) esta situado en el cuadrante II"
        elif (self.puntoX < 0 and self.puntoY < 0):
            return f"El punto ({self.puntoX},{self.puntoY}) esta situado en el cuadrante III"
        elif (self.puntoX > 0 and self.puntoY < 0):
            return f"El punto ({self.puntoX},{self.puntoY}) esta situado en el cuadrante IV"

    def pendiente(self,p):
        pendiente = (p.puntoY-self.puntoY)/(p.puntoX-self.puntoX)
        return f"La pendiente entre los puntos ({self.puntoX},{self.puntoY}) y ({p.puntoX},{p.puntoY}) es de {pendiente}"

    def distancia(self,p):
        distancia = math.sqrt((p.puntoX-self.puntoX)**2 + (p.puntoY-self.puntoY)**2)
        return f"La pendiente entre los puntos ({self.puntoX},{self.puntoY}) y ({p.puntoX},{p.puntoY}) es de {distancia}"

punto1 = Punto(3,5)
punto2 = Punto(1,-1)

print(punto1.__str__())
print(punto2.__str__())

print(punto1.cuadrante())
print(punto2.cuadrante())

print(punto1.pendiente(punto2))

print(punto1.distancia(punto2))