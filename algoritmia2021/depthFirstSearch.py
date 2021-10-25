bloques = []

def search(grafo,clave,grado):
    global bloques
    if grafo[clave]["registrado"] == 2:
        pass 
    else:
        grafo[clave]['registrado'] = 2
        for key in grafo[clave]["aristas"]:
            if grafo[key]["registrado"] == 0: 
                bloques.append([key,grado+1])
                grafo[key]["registrado"] = 1
            search(grafo,key,grado+1)

grafo = {}
for value in range(5):
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