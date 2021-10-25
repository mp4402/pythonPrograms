class Rectangulo:
    def __init__(self,altura,base):
        self.altura = altura
        self.base = base

    def CalcArea(self) -> int:
        area = self.altura * self.base 
        return "El área del rectángulo es: {}".format(area)
    
    def CalcPerimetro(self) -> int:
        perimetro = 2 * (self.altura + self.base)
        return "El perimetro del rectángulo es: {}".format(perimetro)

class Cuadrado(Rectangulo):
    def ObtenerBase(self) -> int:
        self.altura = forma1.base
        self.base = forma1.base

forma1 = Rectangulo(5, 8)
print(forma1.CalcArea())
print(forma1.CalcPerimetro())
forma2 = Cuadrado(0,0)
forma2.ObtenerBase()
print(f"La altura del cuadrado es: {forma2.altura}, y su base es: {forma2.base}")



