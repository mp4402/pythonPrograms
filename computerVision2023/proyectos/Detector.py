from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import argparse
import pickle
import errno
import sys
import io

def imgview(img, filename = None, k = 13):
    """function used to show images

    Args:
        img (numpy array): image to be shown
        filename (string, optional): name of the image if want to be saved. Defaults to None.
        k (int, optional): shape of the plot to show. Defaults to 13.
    """
    fig,ax1 = plt.subplots(figsize=(k,k))
    
    if len(img.shape)==2:
        ax1.imshow(img, vmin=0, vmax=255, cmap='gray')
    else:
        ax1.imshow(img) 
    plt.axis('off')

    if filename != None:
        plt.savefig(filename)

    plt.show()

def imgnorm(img):
    """Nomalize an image
    Args:
        img (numpy array): Source image
    Returns:
        normalized (numpy array): Nomalized image
    """
    vmin, vmax = img.min(), img.max()
    normalized_values = []
    delta = vmax-vmin

    for p in img.ravel():
        normalized_values.append(255*(p-vmin)/delta)

    normalized  = np.array(normalized_values).astype(np.uint8).reshape(img.shape[0],-1)
    return normalized

def encontrarContornos(image):
    """function used to find the contours of an image

    Args:
        image (numpy array): binarized image in which the contours will be found

    Returns:
        list: list with the contours that open cv findContours function return
    """
    mode = cv.RETR_TREE 
    method = [cv.CHAIN_APPROX_NONE, cv.CHAIN_APPROX_SIMPLE]
    contours, hierarchy = cv.findContours(image, mode, method[0])
    return contours

def binarizarPlaca(image):
    """function that binarized the image of the plate

    Args:
        image (numpy array): image of the plate

    Returns:
        numpy array: image of the plate processed and binarized
    """
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    normalized = imgnorm(imgray)
    binarized = cv.adaptiveThreshold(normalized, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,127,0)
    return binarized

def encontrarPlaca(image):
    """function used to identify the plate in the original image

    Args:
        image (numpy array): original image in which the plate will be identified

    Returns:
        numpy array: original image sliced with the shape of the plate
        list: values of x,y,w,h of the plate found
    """
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    normalized = imgnorm(imgray)
    binarized = cv.adaptiveThreshold(normalized, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,11,2)
    contours = encontrarContornos(binarized)
    contorno = []
    caracteristicas = []
    extent = 0

    for c in contours:
        percent =0.052
        epsilon = percent*cv.arcLength(c,True)
        approx = cv.approxPolyDP(c,epsilon,True)
        x,y,w,h = cv.boundingRect(c)
        area = cv.contourArea(approx)
        if (w>h and area > 4000):
            rect_area = w*h
            extent1 = float(area)/rect_area
            if extent1 > extent:
                extent = extent1
                contorno = c
                caracteristicas = [x,y,w,h]
    if len(caracteristicas) > 0:
        placa = image[caracteristicas[1]:caracteristicas[1]+caracteristicas[3],caracteristicas[0]:caracteristicas[0]+caracteristicas[2]]
    else:
        print("No se pudo obtener la placa")
        placa = im
    return placa, caracteristicas

def encontrarNumeros(image):
    """function that identifies the alphanumeric characters in the plate using opencv contours

    Args:
        image (numpy array): image of the plate

    Returns:
        dictionary: dictionary with the values of x,y,w,h from every alphanumeric chareacters identified
    """
    contours = encontrarContornos(image)
    contorno = []
    extent = 0
    direcciones_y = {}
    tamaño_placa = placa.shape
    area_min = tamaño_placa[0] * tamaño_placa[1] * 0.0045
    altura_min = tamaño_placa[0] * 0.55

    for c in contours:
        percent =0.052
        epsilon = percent*cv.arcLength(c,True)
        approx = cv.approxPolyDP(c,epsilon,True)
        x,y,w,h = cv.boundingRect(c)
        area = cv.contourArea(approx)
        if (w<h and area > area_min and h > altura_min):
            contorno.append(c)
            if (y in direcciones_y):
                direcciones_y[y].append([x,y,w,h,len(contorno)-1])
            elif ((y-1) in direcciones_y):
                direcciones_y[y-1].append([x,y,w,h,len(contorno)-1])
            elif ((y-2) in direcciones_y):
                direcciones_y[y-2].append([x,y,w,h,len(contorno)-1])
            elif ((y-3) in direcciones_y):
                direcciones_y[y-3].append([x,y,w,h,len(contorno)-1])
            elif ((y-4) in direcciones_y):
                direcciones_y[y-4].append([x,y,w,h,len(contorno)-1])
            elif ((y-5) in direcciones_y):
                direcciones_y[y-5].append([x,y,w,h,len(contorno)-1])
            elif ((y+1) in direcciones_y):
                direcciones_y[y+1].append([x,y,w,h,len(contorno)-1])
            elif ((y+2) in direcciones_y):
                direcciones_y[y+2].append([x,y,w,h,len(contorno)-1])
            elif ((y+3) in direcciones_y):
                direcciones_y[y+3].append([x,y,w,h,len(contorno)-1])
            elif ((y+4) in direcciones_y):
                direcciones_y[y+4].append([x,y,w,h,len(contorno)-1])
            elif ((y+3) in direcciones_y):
                direcciones_y[y+5].append([x,y,w,h,len(contorno)-1])
            else:
                direcciones_y[y] = [[x,y,w,h,len(contorno)-1]]

    keys = []
    eliminados = 0
    for key in direcciones_y:
        if len(direcciones_y[key]) < 2:
            for element in direcciones_y[key]:
                contorno.pop(int(element[4]-eliminados))
                keys.append(key)
                eliminados = eliminados + 1

    if len(direcciones_y) > 1:
        for i in direcciones_y:
            if len(direcciones_y[i]) < 3:
                keys.append(i)
                
    for key in keys:
        if (key in direcciones_y):
            direcciones_y.pop(key)

    direcciones_y = OrderedDict(sorted(direcciones_y.items()))

    for i in direcciones_y:
        direcciones_y[i] = sorted(direcciones_y[i], key=lambda x: x[0])


    return direcciones_y

def modelo(placa, numeros):
    """function used to detect the values of the plate with a logistic regression model

    Args:
        placa (numpy array): image of the plate to be sliced to obtain the alphanumeric values
        numeros (dictionary): dictionary with the values of x,y,w,h of the characters of the plate

    Returns:
        string: final string with the return values of the model
    """
    characters = []
    resultado = ""
    linea_placa = list(placa[int(caracteristicas[3]/2),:])
    count_negro = linea_placa.count(0)
    count_blanco = linea_placa.count(255)
    if count_negro > count_blanco:
        placa = cv.threshold(placa,0,255, cv.THRESH_BINARY_INV)[1]

    for keys, values in numeros.items(): 
        for i in values:
            character =  placa[i[1]:i[1]+i[3],i[0]:i[0]+i[2]]
            res = cv.resize(character, dsize=(75, 100), interpolation=cv.INTER_LANCZOS4)
            res_flatten = res.flatten()
            characters.append(res_flatten)
    result = loaded_model.predict(characters)
    
    for x in result: 
        resultado += x
    
    return resultado

def mostrarPlaca(image, resultado):
    """function used to show the final image with the square over the plate and the plate serial

    Args:
        image (numpy array): original image to be drawn on
        resultado (string): text that contains the plate alphanumeric values
    """
    color = (0,255,0)

    print("La placa es: " + str(resultado))

    font = cv.FONT_HERSHEY_SIMPLEX
    org = (caracteristicas[0], caracteristicas[1]-10)
    fontScale = 1.5
    thickness = 2
    image = cv.putText(image, resultado, org, font, fontScale, color, thickness, cv.LINE_AA)
    cv.rectangle(image, (caracteristicas[0], caracteristicas[1]), (caracteristicas[0]+caracteristicas[2], caracteristicas[1]+caracteristicas[3]), color, 3)
    imgview(image)

if __name__ == "__main__":
    # the path of the image is received in console
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=str, required=True,
        help="path to image plot")
    args = vars(ap.parse_args())
    
    # the model is loaded
    loaded_model = pickle.load(open('modelo.sav', 'rb'))

    # read the image
    im = cv.imread(args["p"], cv.IMREAD_COLOR)
    im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
    # find the plate
    placa, caracteristicas = encontrarPlaca(im)
    # if the plate can´t be found the program will quit
    if len(caracteristicas) == 0:
        sys.exit()
    # binarize the image of the plate
    placaBinarized = binarizarPlaca(placa)
    # find the alphanumeric characters in the plate
    numeros = encontrarNumeros(placaBinarized)
    # if the characters can´t be found, the program will quit, otherwise, the characters will be send to the model and shown to the client
    if len(numeros) > 0:
        resultado = modelo(placaBinarized, numeros)
        mostrarPlaca(im, resultado)
    else:
        print("No se pudieron detectar los valores en la placa")
        sys.exit()