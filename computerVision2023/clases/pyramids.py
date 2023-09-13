import cv2 as cv


def imgpyramid(img, scale=0.5, min_size=(8, 8)):
    """ Build an image pyramid usign a generator
    Args: 
        img (numpy array): Source image
        scale (float): Scale factor to apply in the pyramid
        min_size (tuple): Dimension of smalles pyramid level
    
    Returns:
        Generator of pyramid
    """

    yield img

    while True:

        img = cv.resize(img, None,fx=scale, fy=scale, interpolation = cv.INTER_CUBIC)

        if img.shape[0] < min_size[0] or img.shape[1] < min_size[1]:
            break
        # yield the next image in the pyramid
        yield img
 

def pyramidview(img):
    """ View all pyramids generated by imgpyramid()
    """
    for (i, resized) in enumerate(imgpyramid(img)):
	    cv.imshow("Layer {}".format(i + 1), resized)
	    cv.waitKey(0)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-path',type=str, help='Path to image', default='../im/cameraman_face.jpg')
    args = parser.parse_args()

    img = cv.imread(args.path, cv.IMREAD_UNCHANGED)

    if img.shape != None:
        pyramidview(img)
    else:
        print('Image not found at {0}'.format(args.path))
