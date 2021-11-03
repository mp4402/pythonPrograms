bloques = []
peso = 0
pesoAnterior = {}
entrada = 0

def search(grafo,clave):
    global bloques
    global peso
    global entrada
    global pesoAnterior
    entrada = 0 
    bandera = 0
    if grafo[clave]["registrado"] == 2:
        #peso -= pesoAnterior[list(pesoAnterior.keys())[-1]]
        #pesoAnterior.pop(list(pesoAnterior.keys())[-1])
        pass
    else:
        grafo[clave]['registrado'] = 2
        for key in grafo[clave]["aristas"]:
            if bandera == 0:
                peso += grafo[clave]["aristas"][key]
                if grafo[key]["registrado"] == 0: 
                    for i in bloques:
                        if key == i[0]:
                            pesoAnterior[key] = peso
                        else:
                            entrada += 1
                    if entrada == len(bloques):
                        bloques.append([key,peso])
                        pesoAnterior[key] = peso
                    grafo[key]["registrado"] = 1
                    if grafo[key]["aristas"] == {}:
                        peso -= pesoAnterior[list(pesoAnterior.keys())[-1]]
                        pesoAnterior.pop(list(pesoAnterior.keys())[-1])
            search(grafo,key)

grafo = {}
cantidad = int(input("Ingrese la cantidad de vertices a ingresar: "))
for value in range(cantidad):
    grafo[int(input("Ingrese el valor del vertice: "))]={"aristas":{},"registrado":0}
    

for key in grafo:
    condicion = 0
    while condicion == 0:
        print("Las aristas ya ingresadas de " + str(key) + " son: ")
        print(grafo[key]["aristas"])
        valor = int(input("Desea ingrese una arista al vertice " + str(key) +"?  \n 1. Sí \n 2. No \n"))
        if valor == 1:
            arista = int(input("Arista: "))
            peso = int(input("Peso de la arista: "))
            grafo[key]["aristas"][int(arista)] = peso 
        else: 
            condicion = 1
    print("\n")

for key in grafo:
    print(key, ":", grafo[key])

peso = 0
valor = int(input("Ingrese el valor del que desea iniciar: "))
search(grafo,valor)
print(bloques)
for key in grafo:
    print(key, ":", grafo[key])