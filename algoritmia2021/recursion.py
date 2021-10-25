b = int(input("Ingrese un número: "))
n = int(input("Ingreses la potencia: "))
m = int(input("Ingrese el valor del mod: "))

def potencia(b,n,m):
    if n==0:
        return 1
    else: 
        return (b * potencia(b,n-1,m))%m

resultado = potencia(b,n,m)
print("El resultado es : " + str(resultado))