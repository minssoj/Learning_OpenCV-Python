# =================================================
# minso.jeong@daum.net
# 17. 이미지 Contour
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv

def contour():
	img = cv.imread('../Images/18.figure.png')
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	ret, thr = cv.threshold(gray_img, 127, 255, 0)
	_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	cv.drawContours(img, contours, -1, (0, 0, 255), 1)
	cv.imshow('thresh', thr)
	cv.imshow('contour', img)
	cv.waitKey(0)
	cv.destroyAllWindows()
contour()