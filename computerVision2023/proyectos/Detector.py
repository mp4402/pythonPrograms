import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import argparse
import cvlib
import errno
import io

def binarizacion(image):
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binarized = cv.adaptiveThreshold(imgray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,127,0)
    return binarized

def encontrarContornos(image):
    mode = cv.RETR_TREE # contour retrieval mode
    method = [cv.CHAIN_APPROX_NONE, cv.CHAIN_APPROX_SIMPLE] # contour approximation method 
    contours, hierarchy = cv.findContours(image, mode, method[0])
    return contours

def encontrarPlaca(image):
    contours = encontrarContornos(image)
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
                
    placa = im[caracteristicas[1]:caracteristicas[1]+caracteristicas[3],caracteristicas[0]:caracteristicas[0]+caracteristicas[2]]
    return placa

def encontrarNumeros(image):
    contours = encontrarContornos(image)
    contorno = []
    extent = 0

    for c in contours:
        percent =0.052
        epsilon = percent*cv.arcLength(c,True)
        approx = cv.approxPolyDP(c,epsilon,True)
        x,y,w,h = cv.boundingRect(c)
        area = cv.contourArea(approx)
        if (w<h and area > 300): 
            contorno.append(c)

    return contorno

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", type=str, required=True,
        help="path to image plot")
    args = vars(ap.parse_args())
    color = (0,255,0)

    im = cv.imread(args["p"], cv.IMREAD_COLOR)
    binarized = binarizacion(im)
    placa = encontrarPlaca(binarized)
    numeros = encontrarNumeros(binarizacion(placa))
    cvlib.imgview(cv.drawContours(placa.copy(), numeros, -1, color, 1))