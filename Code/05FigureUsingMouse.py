import numpy as np
import cv2 as cv
#import matplotlib.pyplot as plt
from random import shuffle
import math

# mode(1): rectangle, mode(0):circle
mode, drawing = True, False
ix, iy = -1, -1
b = [i for i in range(256)]
g = [i for i in range(256)]
r = [i for i in range(256)]

def onMouse1(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK: # 좌클릭 두번
        shuffle(b), shuffle(g), shuffle(r)
        cv.circle(param, (x,y), 50, (b[0], g[0], r[0]), -1)

def onMouse(event, x, y, flags, param):
    global ix, iy, drawing, mode, b, g, r
    if event == cv.EVENT_LBUTTONDOWN:   # 좌클릭 클릭
        drawing = True
        ix, iy = x, y
        shuffle(b), shuffle(g), shuffle(r)
    
    elif event == cv.EVENT_MOUSEMOVE:   # 마우스 이동
        if drawing:
            if mode:
                cv.rectangle(param, (ix,iy),(x,y), (b[0], g[0], r[0]), -1)
            else:
                radious = (ix-x)**2 + (iy-y)**2
                radious = int(math.sqrt(radious))
                cv.circle(param, (ix,iy),radious, (b[0], g[0], r[0]), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(param, (ix,iy),(x,y), (b[0], g[0], r[0]), -1)
        else:
            radious = (ix-x)**2 + (iy-y)**2
            radious = int(math.sqrt(radious))
            cv.circle(param, (ix,iy),radious, (b[0], g[0], r[0]), -1)

def mouseBrush():
    global mode
    img = np.zeros((512,512,3), np.uint8)
    cv.namedWindow('FigureMouse')
    cv.setMouseCallback('FigureMouse', onMouse, param=img)
    
    while True:
        cv.imshow('FigureMouse', img)
        k = cv.waitKey(1) & 0xFF
        
        if k == 27:
            break
        elif k == ord('m'): #change mode
            mode = not mode

    cv.destroyAllWindows()

mouseBrush()