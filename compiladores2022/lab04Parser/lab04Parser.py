#Diccionario principal con la tabla del parser incluida
dict = {
        'S0': {'+': 'ERR',
            '(': 'ERR',
            ')': 'ERR',
            '$': 'ERR',
            'int': 'SHIFTTOS2',
            'E': 'GOTOS1'},
        'S1': {'+': 'SHIFTTOS3',
            '(': 'ERR',
            ')': 'ERR',
            '$': 'ACCEPT',
            'int': 'ERR',
            'E': 'ERR'},
        'S2': {'+': 'REDUCE3',
            '(': 'REDUCE3',
            ')': 'REDUCE3',
            '$': 'REDUCE3',
            'int': 'REDUCE3',
            'E': 'REDUCE3'},
        'S3': {'+': 'ERR',
            '(': 'SHIFTTOS4',
            ')': 'ERR',
            '$': 'ERR',
            'int': 'ERR',
            'E': 'ERR'},
        'S4': {'+': 'ERR',
            '(': 'ERR',
            ')': 'ERR',
            '$': 'ERR',
            'int': 'SHIFTTOS2',
            'E': 'GOTOS5'},
        'S5': {'+': 'SHIFTTOS3',
            '(': 'ERR',
            ')': 'SHIFTTOS6',
            '$': 'ERR',
            'int': 'ERR',
            'E': 'ERR'},
        'S6': {'+': 'REDUCE2',
            '(': 'REDUCE2',
            ')': 'REDUCE2',
            '$': 'REDUCE2',
            'int': 'REDUCE2',
            'E': 'REDUCE2'}
}

#Definicion de clase de la estructura 'Stack' (Last in, first out)
class Stack:
    #Constructor, no requiere de iniciar con un valor de entrada
    def __init__(self):
        self.elements = []

    #Añadido de data al stack, parametro data = Cualquier variable
    def push(self, data):
        self.elements.append(data)
    
    #Eliminacion del ultimo elemento añadido (el que esta a la cima)
    def pop(self):
        #Se verifica que tenga elementos para no generar errores
        if self.elements:
            return self.elements.pop()
        else:
            return None

    #Funcion para obtener el tamaño del stack
    def size(self):
        return len(self.elements)

    #Esta funcion nos retorna el ultimo valor ingresado, solo lo retorna, no lo elimina
    def peek(self):
        return self.elements[-1]

#Definicion de stacks utilizados en el parser
estados = Stack()
producciones = Stack()

#Valores iniciales de los stack, siempre iniciamos con 'S0' en los estados y con '$' en las producciones
estados.push("S0")
producciones.push("$")

#Funcion utilizada para recorrer a traves de la expresion
#Recibe:
#key <- valor en el que se va a posicionar como key dentro de dict
#puntero <- posicion en la que tomaremos la letra para evaluarlo dentro del diccionario
def recorrer(texto, key, puntero):
    #Utilizamos dict, estados y producciones como variables globales
    global dict, estados, producciones

    #Se obtiene la letra que viene del texto
    letra = texto[puntero:puntero+1]
    #Si la letra obtenida es i, tomamos 3 en total para tomar 'int'
    if letra == 'i':
        letra = texto[puntero:puntero+3]
    
    #Se verifica si ya se acabo el recorrido del texto
    if letra == "":
        return (key,puntero)

    #Se veridica si la letra que viene se encuentra dentro del diccionario
    if dict[key].get(letra) == None:
        #Retornamos un mensaje de error con la letra no valida
        print("ERROR: " + letra + " no es un input valido")
        return

    if dict[key][letra] == "ERR":
        return ("ERR",puntero)
    else:
        #Ingresamos la produccion al stack producciones
        producciones.push(letra)

        #Verificamos si se ha completado la produccion, es decir, si lo construido obtenemos un accept
        if(dict[key][letra] == "ACCEPT"):
            return

        #Redefinimos key con el nuevo camino potencial segun en que estado estemos y cual produccion ingresa
        key = dict[key][letra]

        #Si en el resultado obtenemos un 'Go To', añadimos el estado al que nos dirigiremos al stack de 
        #estados y redefinimos la key como este estado, sin el texto de la accion
        if(key[0:4]=="GOTO"):
            estados.push(key[4:6])
            key = estados.peek()

        #Si en el resultado obtenemos un 'Shift To', añadimos el estado al que nos dirigiremos al stack de 
        #estados y redefinimos la key como este estado, sin el texto de la accion
        if(key[0:7]=="SHIFTTO"):
            estados.push(key[7:9])
            key = estados.peek()

        #Si al estado al que nos dirigimos a continuacion incluye la palabra 'Reduce' reducimos la expresion
        #en los stacks
        if(dict[estados.peek()][producciones.peek()][0:6]=="REDUCE"):

            #Verificamos si es un reduce a la produccion 2 ['<E> -> <E> + (<E>)']
            if(dict[estados.peek()][producciones.peek()][6:7]=='2'):
                #Realizamos la eliminacion de producciones y estados previos
                for i in range(5):
                    producciones.pop()
                    estados.pop()

                #Ingresamos la produccion por la que se reduce
                producciones.push("E")

            #Verificamos si es un reduce a la produccion 3 ['<E> -> int']
            if(dict[estados.peek()][producciones.peek()][6:7]=='3'):
                #Realizamos la eliminacion de producciones y estados previos
                producciones.pop()
                estados.pop()

                #Ingresamos la produccion por la que se reduce
                producciones.push("E")
            
            #Por ultimo, obtenemos la nueva key a la que nos dirigiremos despues de la reduccion
            key = dict[estados.peek()][producciones.peek()]
            #Obtenemos unicamente su valor (es decir solo S0, S1, etc.)
            key = key[len(key)-2:len(key)]
            #Añadimos este estado al stack de estados
            estados.push(key)
        #Si letra es int, avanzamos en el diccionario y aumentamos en 3 el puntero
        if letra == 'int':
            return recorrer(texto,key,puntero+3)
        #De lo contrario, avanzamos en el diccionario y aumentamos en 1 el puntero 
        return recorrer(texto,key,puntero+1)

#Funcion principal, no recibe parametros
def main():
    #Utilizamos estados y producciones como variables globales 
    global estados, producciones
    #Iniciamos el puntero para texto
    inicio = 0
    #Establecemos la key para recorrer dict desde el inicio
    key = 'S0'
    #Creamos el menu para el ingreso
    opcion = int(input("""Si desea usar el ejemplo [int+(int)+(int)], ingrese 1
Si desea ingresar su produccion ingrese 2
Valor: """))
    #texto-> El texto que se va a evaluar
    #Validamos la seleccion obtenida en opcion
    if(opcion==1):
        texto = texto = "int+(int)+(int)$"
    elif(opcion == 2):
        texto = input("""\nLos valores admitidos son:
1. int
2. E
3. +
4. (
5. )
IMPORTANTE: al final siempre incluir '$'
El programa no identifica mayusculas o minusculas, favor ingresar como se especifico arriba
Ingrese su produccion: """)
    else:
        print("Ingrese una opcion valida")
        return
    #Llamamos a la funcion para recorrer
    recorrer(texto,key,inicio)
    #Si el último estado guardado es diferente a 'S1', y la última produccion guardada no es '$', no es ACCEPT
    #por lo tanto, error
    if(dict[estados.peek()][producciones.peek()] != "ACCEPT"):
        print("Producción no valida")
    #Si el último estado guardado es 'S1', y la última produccion guardada '$', es ACCEPT, por lo tanto, es valido
    else:
        print("Producción valida")
    return

#Inicio del programa
main()