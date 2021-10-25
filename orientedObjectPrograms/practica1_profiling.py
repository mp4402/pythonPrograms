import cProfile


def sumatoria():
    numero = int(input("Ingrese un número para el límite de la sumatoria: "))
    control = 1
    total = 0
    while (control <= numero):
        total += control
        control+=1
    print("La sumatoria desde el 1 hasta el " + str(numero) + " es: " + str(total))

cProfile.run('sumatoria()')