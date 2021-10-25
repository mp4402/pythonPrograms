class Complex():
    def __init__(self,r=0,i=0) -> None:
        self.real = r
        self.imag = i

    def __str__(self) -> str:
        operand = "+"
        if (self.imag < 0):
            operand = ""
        return f"{self.real}, {operand} {self.imag}j"

    def conjugate(self):
        pass

z = Complex(1,-2)
z.imag()
print(z)