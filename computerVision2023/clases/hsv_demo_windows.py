import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

def open_video_src():
    cap = cv.VideoCapture(0)
    return cap

def get_frame(cap):
    _, frame = cap.read()
    #frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    return frame

def hsv_split(frame):
    hsv = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
    
    # H value in opencv between 0 and 180
    # https://cvexplained.wordpress.com/2020/04/28/color-detection-hsv/#:~:text=In%20OpenCV%2C%20Hue%20has%20values,255%2C%200%2D255).
    lower_boundary = np.array([95,100,100])
    upper_boundary = np.array([130,255,255])

    mask = cv.inRange(hsv, lower_boundary, upper_boundary)
    res = cv.bitwise_and(frame,frame, mask= mask)
    return mask, res

cap = open_video_src()
#cap.set(cv.CAP_PROP_FRAME_WIDTH, 40)
#cap.set(cv.CAP_PROP_FRAME_HEIGHT, 30)

frame = get_frame(cap)
#frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
mask, res = hsv_split(frame)

# create windows
win0 = 'Original'
win1 = 'Processed'
cv.namedWindow(win0, cv.WINDOW_NORMAL)
cv.namedWindow(win1, cv.WINDOW_NORMAL)

r,c = frame.shape[0:2]
resize_factor = 2

R = int(r//resize_factor)
C = int(c//resize_factor)
win_size = (C, R) 

cv.resizeWindow(win0, (win_size[0]//2,win_size[1]//2))
cv.resizeWindow(win1, win_size)

cv.imshow(win0, frame)
cv.imshow(win1, mask)

# align windows        
cv.moveWindow(win1, 0, 0)
cv.moveWindow(win0, C, 0)
while True:

    frame = get_frame(cap)
    mask, res = hsv_split(cv.cvtColor(frame, cv.COLOR_BGR2RGB))
    res = cv.cvtColor(res, cv.COLOR_RGB2BGR)
    win_size = (C, R) 

    cv.resizeWindow(win0, (win_size[0]//2,win_size[1]//2))
    cv.resizeWindow(win1, win_size)

    cv.imshow(win0, frame)
    cv.imshow(win1, res)

    # align windows        
    cv.moveWindow(win1, 0, 0)
    cv.moveWindow(win0, C, 0)
    
    # exit with q
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.close()