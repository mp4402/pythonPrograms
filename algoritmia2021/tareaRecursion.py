#Mario Enrique Pisquiy Gómez    Carné 20200399
from os import system
condicion = 0

def euclidesMCD(a, b):
	if b == 0: return a
	return euclidesMCD(b, a%b)

def productoSumasPositivos(n,x):
    if x==0:
        return 0
    else:
        return n+productoSumasPositivos(n,x-1)

def productoSumasNegativos(n,x):
    if x==0:
        return 0
    else:
        return n+productoSumasNegativos(n,x+1)

def sumaImpares(n):
    if n == 1:
        return 1
    else:
        return n + sumaImpares(n-2)

def numeroMenor(vector):
    if len(vector) == 1:
        return vector[0]
    else:
        m = numeroMenor(vector[1:])
        return m if m < vector[0] else vector[0]

while condicion == 0:
    opcion = int(input("Menú de opciones\n1.Obtener el mcd\n2.Multiplicación con sumas\n3.Suma de números impares\n4.Encontrar el valor mínimo\n5.Salir\nIngrese la opcion que desee: "))
    if opcion==1:
        system("cls")
        a=int(input("Ingrese el primer valor: "))
        b=int(input("Ingrese el segundo valor: "))
        print("El mcd de " + str(a) + " y " + str(b) + " es: " + str(euclidesMCD(a,b)) + "\n")
    elif opcion==2:
        system("cls")
        n=int(input("Ingrese el primesr multiplicando: "))
        x=int(input("Ingrese el segundo multiplicando: "))
        if x < 0:
           print("El resultado es: " + str(-productoSumasNegativos(n,x)) + "\n") 
        else:
            print("El resultado es: " + str(productoSumasPositivos(n,x)) + "\n") 
    elif opcion==3:
        system("cls")
        n=int(input("Ingrese la cantidad de números positios impares que sesea sumar: "))
        print("La suma de los primeros " + str(n) + " impares es: " + str(sumaImpares((n*2)-1)) + "\n")
    elif opcion==4:
        system("cls")
        condicionVector = 0
        vector=[]
        while condicionVector==0:
            system("cls")
            n = int(input("1.Ingresar un número al conjunto\n2.Dejar de ingresar valores\nIngrese la opción deseada: "))
            if n ==1:
                vector.append(int(input("Ingrese el valor deseado: ")))
            elif n==2:
                condicionVector=1
            else:
                print("Por favor ingrese una opción valida")
        print("El valor menor de los datos ingresados es: " + str(numeroMenor(vector)) + "\n")
    elif opcion==5:
        system("cls")
        print("Gracias por utlizar este programa")
        condicion = 1 
    else:
        system("cls")
        print("Ingrese una opcion correcta")