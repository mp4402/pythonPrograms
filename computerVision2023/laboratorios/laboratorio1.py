import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import errno
import cvlib
import sys
import io

def imgPrep(img):
    """Función utilizada para preprocesar la imagen

    Args:
        img (np.ndarray): imagen a procesar

    Raises:
        TypeError: error devuelto en caso de enviar un tipo de dato incorrecto (np.ndarray)

    Returns:
        np.ndarray: imagen procesada
    """
    if type(img) != np.ndarray:
        raise TypeError("'img' must be an numpy.ndarray")

    thresh_val = 135
    binarized = cv.threshold(img,thresh_val,255, cv.THRESH_BINARY_INV)[1]
    kernel = np.array([[0, 255, 0],
                   [255, 255, 255],
                   [0, 255, 0]], np.uint8)
    erosion = cv.erode(binarized, kernel, iterations=1)
    return erosion

def imgpad(img, r):
    """Función utilizada para realizar el pad de la imagen

    Args:
        img (np.ndarray): array de numpy que contiene los valores de la imagen
        r (int): número que representa el ancho del marco que se desea aplicar a la imagen

    Raises:
        TypeError: error devuelto en caso de enviar un tipo de dato incorrecto (int)
        TypeError: error devuelto en caso de enviar un tipo de dato incorrecto (np.ndarray)

    Returns:
        np.ndarray: array de numpy con la imagen procesada
    """
    if type(r) != int:
        raise TypeError("'r' must be an integer")

    if type(img) != np.ndarray:
        raise TypeError("'img' must be an numpy.ndarray")

    shapeY, shapeX = img.shape
    newShapeY = shapeY + (2*r)
    newShapeX = shapeX + (2*r)

    newImage = np.ndarray((newShapeY,newShapeX), buffer=np.zeros(newShapeX*newShapeY),offset=np.int_().itemsize,dtype=int)

    for i in range(shapeY):
        modifiedRow = np.append(np.zeros(r), img[i])
        modifiedRow = np.append(modifiedRow, np.zeros(r))
        np.copyto(newImage[i+r,:],modifiedRow,casting='unsafe')
        
    return newImage

class UnionFind:
    """clase utilizada para encontrar los padres de cada estructura (disjoint structures)
    """
    def __init__(self, numOfElements):
        """Constructor de la clase

        Args:
            numOfElements (int): número de etiquetas en la imagen
        """
        self.parent = self.makeSet(numOfElements)
        self.size = [1]*numOfElements
        self.count = numOfElements

    def makeSet(self, numOfElements):
        return [x for x in range(numOfElements)]

    def find(self, node):
        """Función utilizada para encontrar el padre de un nodo en especifico 

        Args:
            node (int): valor del nodo del que se busca padre (raíz)

        Returns:
            node: nodo padre (raíz) del nodo recibido
        """
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, node1, node2):
        """Función utilizada para buscar y asignar el nodo padre de cada estructura

        Args:
            node1 (int): nodo 1 de la estructura
            node2 (int): nodo 2 de la estructura
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return

        if self.size[root1] > self.size[root2]:
            self.parent[root2] = root1
            self.size[root1] += 1
        else:
            self.parent[root1] = root2
            self.size[root2] += 1
        
        self.count -= 1

def neighbor(row,column,label):
    """función utilizada para hallar los vecinos del elemento de la imagen

    Args:
        row (int): fila en la que se encuentra el indice
        column (int): columna en la que se encuentra el indice
        label (np.np.ndarray): matriz de la imagen que se está procesando

    Returns:
        list: lista con los valores de los vecinos del elemento de la imagen
    """
    left = label[row-1,column]
    above = label[row,column-1]
    neighbor_array = [left,above]
    return neighbor_array

def connected_c(img):
    """función utilizada para hallar las etiquetas de los objetivos en la imagen

    Args:
        img (np.ndarray): matriz de la imagen que se está procesando

    Raises:
        TypeError: error devuelto en caso de enviar un tipo de dato incorrecto (np.ndarray)

    Returns:
        np.ndarray: matriz con las etiquetas para cada grupo objetivo en la imagen
    """
    if type(img) != np.ndarray:
        raise TypeError("'img' must be an numpy.ndarray")
        return

    shapeY, shapeX = img.shape
    label = np.zeros([shapeY,shapeX])
    links = []
    new = 1
    #first pass
    for row in range(shapeY):
        for column in range(shapeX):
            if img[row,column] != [0]:
                current_neighbor = neighbor(row,column,label)
                if current_neighbor == [0,0]:
                    label[row, column] = new
                    new = new + 1
                else :
                    if np.min(current_neighbor) == 0 or current_neighbor[0] == current_neighbor[1] :
                        label[row,column] = np.max(current_neighbor)
                    else:
                        label[row,column] = np.min(current_neighbor)
                        links.append([np.max(current_neighbor), np.min(current_neighbor)])

    #second pass
    uf = UnionFind(new)

    for node1, node2 in links:
        uf.union(node1.astype(int), node2.astype(int))

    for i in range(new):
        label[label==i] = uf.find(i)

    return label

def get_random_color():
    """función utilizada para obtener un número aleatorio para asignar un color

    Returns:
        list: lista con los valores para crear un color (r,g,b) para la etiqueta deseada
    """
    return list(np.random.choice(range(256), size=3))

def labelview(img,filename = None, size=13):
    """función utilizada para asignar los colores a cada etiqueta y mostrar la imagen resultante

    Args:
        img (np.ndarray): imagen procesada con connected_c y lista para asignar colores a cada etiqueda
        filename (str, optional): nombre de la imagen para ser guardada. Defaults to None.
        size (int, optional): tamaño de la imagen final. Defaults to 13.
    """
    componentes = np.unique(img)
    colores = {0:[0, 0, 0]}

    # get the random color for the label
    for i in componentes:
        if i != 0: 
            colores[i] = get_random_color()       

    shapeY, shapeX = img.shape

    img_res = []

    for row in range(0, shapeY):
        new_row = []
        for column in range(0, shapeX): 
            # se asigna el color que corresponde a su segmento
            segment = img[row, column]
            new_row.append(colores[segment])

        img_res.append(new_row)
    img_res = np.array(img_res)

    if filename is not None: 
        cvlib.imgview(img_res, filename = filename)
    else:
        cvlib.imgview(img_res,k=size)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("""You must write the name of the image and the output name:
        For example: python laboratorio_1.py image_name.pgm output_name.png""")
        sys.exit()
    im = cv.imread(sys.argv[1], cv.IMREAD_COLOR)
    img = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
    newImage = imgPrep(img)
    newImageCC = connected_c(newImage)
    labelview(newImageCC,size=50,filename=sys.argv[2])
