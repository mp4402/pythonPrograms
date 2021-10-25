bloques = []

def search(grafo,clave,grado):
    global bloques
    if grafo[clave]["registrado"] == 2:
        pass 
    else:
        grafo[clave]['registrado'] = 2
        bandera = 0
        for key in grafo[clave]["aristas"]:
            if grafo[key]['registrado'] == 0:
                grafo[key]['registrado'] = 1
                bandera = 1
                bloques.append([key,grado+1])
        for key in grafo[clave]["aristas"]: 
            if bandera == 1:
                search(grafo,key,grado+1)
            else:
                search(grafo,key,grado)

grafo = {}
cantidad = int(input("Ingrese la cantidad de vertices a ingresar: "))
for value in range(cantidad):
    grafo[int(input("Ingrese el valor del vertice: "))]={"aristas":[],"registrado":0}

for key in grafo:
    condicion = 0
    while condicion == 0:
        print("Las aristas ya ingresadas de " + str(key) + " son: ")
        print(grafo[key]["aristas"])
        valor = int(input("Desea ingrese una arista al vertice " + str(key) +"?  \n 1. Sí \n 2. No \n"))
        if valor == 1:
            arista = int(input("Arista: "))
            grafo[key]["aristas"].append(arista)
            grafo[arista]["aristas"].append(key)
        else: 
            condicion = 1
    print("\n")

for key in grafo:
    print(key, ":", grafo[key])

search(grafo,1,0)
print(bloques)
for key in grafo:
    print(key, ":", grafo[key])