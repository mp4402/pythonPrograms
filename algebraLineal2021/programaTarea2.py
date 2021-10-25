import random
num1 = int(random.randint(1,99))
num2 = int(random.randint(1,99))
print("El valor de la variable 'num1' " + str(num1))
print("El valor de la variable 'num2' " + str(num2)+"\n")

Operaciones = ["suma","resta","multiplicación","división","potencia"]
Resultados = [num1+num2,num1-num2,num1*num2,num1/num2,num1**num2]
for n in range(0,5):
    print("La " + Operaciones[n] + " entre " + str(num1) + " y " + str(num2) + " es " + str(Resultados[n]))

print("\n")

matriz = []
for x in range(7):
    matriz.append([])
    for y in range(7):
        matriz[x].append(random.randint(1,99)) 

for x in matriz:
    print(x)

print("\n")

for x in range(7):
    matriz[x][x] = random.randint(1,99)

for x in matriz:
    print(x)