import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def hist(img):
    #Aún falta modificar para imagenes a color
    k=8
    fig = plt.figure(figsize=(k,k))
    
    ax1 = fig.add_subplot(2,2,1)
    ax1.imshow(img,cmap='gray',vmin=0,vmax=255)
    plt.axis('off')

    ax2 = fig.add_subplot(2,2,2)
    ax2.set_title("Histogram")
    ax2.set_xlabel("Pixel Count")
    ax2.set_ylabel("Pixel Vount")
    ax2.set_facecolor("black")
    histr = cv.calcHist([img],[0],None,[256],[0,256])
    ax2.plot(histr, c="white",linewidth=0.6)

    plt.plot()
    
def imgview(img):
    k=13
    fig = plt.figure(figsize=(k,k))
    ax1 = fig.add_subplot(2,2,1)

    if (len(img.shape)>2):
        ax1.imshow(img)
    else:
        ax1.imshow(img,cmap='gray',vmin=0,vmax=255)

    plt.axis('off')
    plt.plot()

def imgcmp(img1, img2, titles):
    if len(titles) < 2:
        return 0

    k=8
    fig = plt.figure(figsize=(k,k))
    
    ax1 = fig.add_subplot(2,2,1)
    ax1.set_title(titles[0])
    plt.axis('off')
    ax2 = fig.add_subplot(2,2,2)
    ax2.set_title(titles[1])
    plt.axis('off')

    if (len(img.shape)>2):
        ax1.imshow(img)
        plt.axis('off')
        ax2.imshow(img)
        plt.axis('off')
    else:
        ax1.imshow(img,cmap='gray',vmin=0,vmax=255)
        
        ax2.imshow(img,cmap='gray',vmin=0,vmax=255)
    
    plt.plot()
