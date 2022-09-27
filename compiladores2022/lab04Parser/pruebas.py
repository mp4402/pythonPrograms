from cgitb import text
from fileinput import filename
from pickle import FALSE, TRUE
import re
from string import octdigits
from tkinter.tix import INTEGER
from typing import final

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

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)
    
    def pop(self):
        if self.elements:
            return self.elements.pop()
        else:
            return None

    def size(self):
        return len(self.elements)

    def peek(self):
        return self.elements[-1]

estados = Stack()
producciones = Stack()
estados.push("S0")
producciones.push("$")

class Node:
   def __init__(self, tipo, palabra, fila, columna):
      self.tipo = tipo
      self.palabra = palabra
      self.fila = fila 
      self.columna = columna
      self.nextnodo = None

class SLinkedList:
   def __init__(self):
      self.headval = None
# Function to add newnode
   def AtEnd(self, tip, pal, fil, col):
      NewNode = Node(tip, pal, fil, col)
      if self.headval is None:
         self.headval = NewNode
         return
      laste = self.headval
      while(laste.nextnodo):
         laste = laste.nextnodo
      if laste.tipo == "Error" and NewNode.tipo == "Error":
        laste.palabra = laste.palabra + pal
        laste.columna = laste.columna + 1
      else:
        laste.nextnodo=NewNode
# Print the linked list
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print("-----NODO-----")
         print (f"Tipo: {printval.tipo} - Palabra: {printval.palabra} - Fila: {printval.fila} - Columna: {printval.columna}" )
         printval = printval.nextnodo

lista = SLinkedList()

#Funcion que recorre el diccionario a partir de un key
def recorrer(texto, key, puntero):
    global dict, estados, producciones

    #Se obtiene la letra que viene del texto
    letra = texto[puntero:puntero+1]
    if letra == 'i':
        letra = texto[puntero:puntero+3]
    
    #Se verifica si ya se acabo el recorrido del texto
    if letra == "":
        return (key,puntero)
    
    #Verificar si la letra se encuentra dentro de una expresion regular
#    bandera = 1
#    for k in dict[key].keys():
#        if re.search(str(k), str(letra)):
#            letra = k
#            bandera = 0
#            break
#    if bandera:
#        return ("ERR",puntero)


    #Se veridica si la letra que viene se encuentra dentro del diccionario
    if dict[key][letra] == "ERR":
        return ("ERR",puntero)
    else:
        producciones.push(letra)
        if(dict[key][letra] == "ACCEPT"):
            return
        key = dict[key][letra]
        if(key[0:4]=="GOTO"):
            estados.push(key[4:6])
            key = estados.peek()
        if(key[0:7]=="SHIFTTO"):
            estados.push(key[7:9])
            key = estados.peek()
        if(dict[estados.peek()][producciones.peek()][0:6]=="REDUCE"):
            if(dict[estados.peek()][producciones.peek()][6:7]=='2'):
                for i in range(5):
                    producciones.pop()
                    estados.pop()
                producciones.push("E")
            if(dict[estados.peek()][producciones.peek()][6:7]=='3'):
                producciones.pop()
                producciones.push("E")
                estados.pop()
            key = dict[estados.peek()][producciones.peek()]
            key = key[len(key)-2:len(key)]
            estados.push(key)
        if letra == 'int':
            return recorrer(texto,key,puntero+3)
        return recorrer(texto,key,puntero+1)


#def nodo_informacion(texto,inicio):
#    global lista
#    tamaño = len(finales.keys())
#    if  tamaño > 1:
        #print("------ nodo -----")
        #print("Palabra: " + texto[inicio:list(finales)[-1]])
        #print("Type: " + finales[list(finales)[-1]][0]) 
        #print(f"Columna: {list(finales)[-1] - 1}") #key,class
#        lista.AtEnd(finales[list(finales)[-1]][0], texto[inicio:list(finales)[-1]], 1, (list(finales)[-1] - 1))
#        return (list(finales)[-1])
#    elif tamaño == 1:
        #print("------ nodo -----")
        #print("Palabra: " + texto[inicio:list(finales)[-1]])
        #print("Type: " + finales[list(finales)[0]][0])  
        #print(f"Columna: {list(finales)[-1] - 1}")  #key,class
#        lista.AtEnd(finales[list(finales)[0]][0], texto[inicio:list(finales)[-1]], 1, (list(finales)[-1] - 1))
#        return (list(finales)[0])
#    else:
        #print("------ nodo -----")
        #print("Palabra: " + texto[inicio:inicio+1])
        #print("Type: " + "Error")  #key,class
        #print(f"Columna: {inicio - 1}")  
#        lista.AtEnd("Error", texto[inicio:inicio+1], 1, inicio)
#        return (inicio+1)


#Funcion principal que agrupa todas las funciones
def main():
    global estados, producciones
    inicio = 0
    key = 'S0'
    llave = 0
    #El texto que se va a evaluar
    texto = "int+(E)+(int)$"
    texto_tamaño = len(texto)
    while (llave == 0):
        #funcion para recorrer el diccionario
        recorrer(texto,key,inicio)
        llave = 1
    if(dict[estados.peek()][producciones.peek()] != "ACCEPT"):
        print("Producción no valida")
    else:
        print("Producción valida")
#    lista.listprint()






main()
#texto = "double"
#letra = texto[0:1]
#print(dict['A'][letra])