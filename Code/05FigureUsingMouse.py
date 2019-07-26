import numpy as np
import cv2 as cv
#import matplotlib.pyplot as plt
from random import shuffle

b = [i for i in range(256)]
g = [i for i in range(256)]
r = [i for i in range(256)]

def onMouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK: # 좌클릭 두번
        shuffle(b), shuffle(g), shuffle(r)
        cv.circle(param, (x,y), 50, (b[0], g[0], r[0]), -1)

def mouseBrush():
    img = np.zeros((512,512,3), np.uint8)
    cv.namedWindow('FigureMouse')
    cv.setMouseCallback('FigureMouse', onMouse, param=img)
    
    while True:
        cv.imshow('FigureMouse', img)
        k = cv.waitKey(1) & 0xFF
        
        if k == 27:
            break
    cv.destroyAllWindows()

mouseBrush()