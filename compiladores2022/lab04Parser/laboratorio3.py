from cgitb import text
from fileinput import filename
from pickle import FALSE, TRUE
import re
from string import octdigits
import string
from tkinter.tix import INTEGER
from typing import final

dict = {
        'A': {'[>,+,-,*,/,%]':'B',
            '[1-9]': 'C',
            '[A-Fa-f]': 'D',
            '[G-WY-Zg-wy-z]': 'E',
            '0': 'F',
            '[xX]': 'G'},
        'B': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'ERR',
            '[A-Fa-f]': 'ERR',
            '[G-WY-Zg-wy-z]': 'ERR',
            '0': 'ERR',
            '[xX]': 'ERR'},
        'C': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'ERR',
            '[A-Fa-f]': 'ERR',
            '[G-WY-Zg-wy-z]': 'ERR',
            '0': 'ERR',
            '[xX]': 'ERR'},
        'D': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'H',
            '[A-Fa-f]': 'I',
            '[G-WY-Zg-wy-z]': 'I',
            '0': 'H',
            '[xX]': 'I'},
        'E': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'H',
            '[A-Fa-f]': 'I',
            '[G-WY-Zg-wy-z]': 'I',
            '0': 'H',
            '[xX]': 'I'},
        'F': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'H',
            '[A-Fa-f]': 'I',
            '[G-WY-Zg-wy-z]': 'I',
            '0': 'H',
            '[xX]': 'J'},
        'G': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'H',
            '[A-Fa-f]': 'I',
            '[G-WY-Zg-wy-z]': 'I',
            '0': 'H',
            '[xX]': 'I'},
        'H': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'H',
            '[A-Fa-f]': 'I',
            '[G-WY-Zg-wy-z]': 'I',
            '0': 'H',
            '[xX]': 'I'},
        'I': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'H',
            '[A-Fa-f]': 'I',
            '[G-WY-Zg-wy-z]': 'I',
            '0': 'H',
            '[xX]': 'I'},
        'J': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'K',
            '[A-Fa-f]': 'L',
            '[G-WY-Zg-wy-z]': 'ERR',
            '0': 'ERR',
            '[xX]': 'ERR'},
        'K': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'M',
            '[A-Fa-f]': 'N',
            '[G-WY-Zg-wy-z]': 'ERR',
            '0': 'M',
            '[xX]': 'ERR'},
        'L': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'M',
            '[A-Fa-f]': 'N',
            '[G-WY-Zg-wy-z]': 'ERR',
            '0': 'M',
            '[xX]': 'ERR'},
        'M': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'M',
            '[A-Fa-f]': 'N',
            '[G-WY-Zg-wy-z]': 'ERR',
            '0': 'M',
            '[xX]': 'ERR'},
        'N': {'[>,+,-,*,/,%]':'ERR',
            '[1-9]': 'M',
            '[A-Fa-f]': 'N',
            '[G-WY-Zg-wy-z]': 'ERR',
            '0': 'M',
            '[xX]': 'ERR'},
        'FINALES':{
            'B': 'ARITH_OP',
            'C': 'DIGIT',
            'D': 'ALPHA',
            'E': 'ALPHA',
            'F': 'DIGIT',
            'G': 'APLHA',
            'H': 'ID',
            'I': 'ID',
            'K': 'HEX_LITERAL',
            'L': 'HEX_LITERAL',
            'M': 'HEX_LITERAL',
            'N': 'HEX_LITERAL'
        }
        
}

finales = {}
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
        return
      elif NewNode.palabra == " ":
        return
      else:
        laste.nextnodo=NewNode
        return
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
    global dict, finales 

    #Finales por las que pasa la palabra        
    if key in dict['FINALES'].keys():
        if puntero not in finales.keys():
            finales[puntero] = [dict['FINALES'][key]]
        else:
            finales[puntero].apped(dict['FINALES'][key])

    #Se obtiene la letra que viene del texto
    letra = texto[puntero:puntero+1]
    
    #Se verifica si ya se acabo el recorrido del texto
    if letra == "":
        return (key,puntero)
    
    #Verificar si la letra se encuentra dentro de una expresion regular
    bandera = 1
    for k in dict[key].keys():
        if re.search(str(k), str(letra)):
            letra = k
            bandera = 0
            break
    if bandera:
        return ("ERR",puntero)

    #Se veridica si la letra que viene se encuentra dentro del diccionario
    if dict[key][letra] == "ERR":
        return ("ERR",puntero)
    else:
        key = dict[key][letra]
        print(dict[key][letra])
        return recorrer(texto,key,puntero+1)
    

def nodo_informacion(texto,inicio,linea):
    global finales, lista
    tamaño = len(finales.keys())
    if  tamaño > 1:
        #print("------ nodo -----")
        #print("Palabra: " + texto[inicio:list(finales)[-1]])
        #print("Type: " + finales[list(finales)[-1]][0]) 
        #print(f"Columna: {list(finales)[-1] - 1}") #key,class
        lista.AtEnd(finales[list(finales)[-1]][0], texto[inicio:list(finales)[-1]], linea, (list(finales)[-1] - 1))
        return (list(finales)[-1])
    elif tamaño == 1:
        #print("------ nodo -----")
        #print("Palabra: " + texto[inicio:list(finales)[-1]])
        #print("Type: " + finales[list(finales)[0]][0])  
        #print(f"Columna: {list(finales)[-1] - 1}")  #key,class
        lista.AtEnd(finales[list(finales)[0]][0], texto[inicio:list(finales)[-1]], linea, (list(finales)[-1] - 1))
        return (list(finales)[0])
    else:
        #print("------ nodo -----")
        #print("Palabra: " + texto[inicio:inicio+1])
        #print("Type: " + "Error")  #key,class
        #print(f"Columna: {inicio - 1}")  
        lista.AtEnd("Error", texto[inicio:inicio+1], linea, inicio)
        return (inicio+1)

        

#Funcion principal que agrupa todas las funciones
def main():
    global finales, lista
    linea = 0
    key = 'A'
    #Leer el texto que se va a evaluar
    with open('entrada.txt') as f:
        for line in f:
            linea+=1
            texto = line.strip()
            texto_tamaño = len(texto)
            inicio = 0
            while (inicio < texto_tamaño):
                #funcion para recorrer el diccionario
                recorrer(texto,key,inicio)
                #print("\n---- Finales ---\n" + str(finales))
                #funcion para obtner el tipo de dato y columna
                inicio = nodo_informacion(texto, inicio,linea)
                #limpiar estrcturas
                finales = {}
    lista.listprint()






main()
#texto = "double"
#letra = texto[0:1]
#print(dict['A'][letra])