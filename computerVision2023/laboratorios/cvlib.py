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

def imgview(img, k = 13):
    fig,ax1 = plt.subplots(figsize=(k,k))
    
    if len(img.shape)==2:
        ax1.imshow(img, vmin=0, vmax=255, cmap='gray')
    else:
        ax1.imshow(img) 
    plt.axis('off')
    plt.show()

def imgcmp(img1, img2, titles = None):
    if titles == None:
        k=8
        fig = plt.figure(figsize=(k,k))
        
        ax1 = fig.add_subplot(2,2,1)
        plt.axis('off')
        ax2 = fig.add_subplot(2,2,2)
        plt.axis('off')

        if (len(img1.shape)>2):
            ax1.imshow(img1)
            plt.axis('off')
            ax2.imshow(img2)
            plt.axis('off')
        else:
            ax1.imshow(img1,cmap='gray',vmin=0,vmax=255)
            ax2.imshow(img2,cmap='gray',vmin=0,vmax=255)
        
        plt.plot()
    else: 
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

        if (len(img1.shape)>2):
            ax1.imshow(img1)
            plt.axis('off')
            ax2.imshow(img2)
            plt.axis('off')
        else:
            ax1.imshow(img1,cmap='gray',vmin=0,vmax=255)
            ax2.imshow(img2,cmap='gray',vmin=0,vmax=255)
        
        plt.plot()


def imgcdf(img):
    """Compute the CDF on an image
    Args: 
        img (numpy array): Source image
    Returns:
        cdf (list): Computed CDf of img
        hist (list): Histogram of img
    """
    hist_list = cv.calcHist([img],[0],None,[256],[0,256])
    #hist = [(item) for sublist in hist_list for item in sublist]
    hist = hist_list.ravel()

    # define cdf placeholder
    cdf = []
    t = 0
    for p in hist:
        t += p
        cdf.append(t)
    return cdf, hist

def imgeq(img):
    """ Equalize a grayscale image
    Args:
        img (numpy array): Grayscale image to equalize
    Returns:
        eq (numpy array): Equalized image
    """
    cdf = imgcdf(img)[0]
    cdf_eq = []
    n = img.shape[0] * img.shape[1]
    m = min(i for i in cdf if i > 0)

    for i in cdf:
        if i >= m:
            cdf_eq.append(int(round(255*(i-m)/(n-m))))
        else:
            cdf_eq.append(0)
    eq = cv.LUT(img, np.array(cdf_eq).astype(np.uint8))
    return eq

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