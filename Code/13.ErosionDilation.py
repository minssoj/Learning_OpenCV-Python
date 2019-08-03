# =================================================
# minso.jeong@daum.net
# 13. 이미지 Erosion과 Dilation
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img_path = '../Images/14.alphabet.jpg'

# A. Erosion & Dilation
def morph():
	img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
	kernel = np.ones((3, 3), np.uint8)
	erosion = cv.erode(img, kernel, iterations=1)
	dilation = cv.dilate(img, kernel, iterations=1)
	cv.imshow('original', img)
	cv.imshow('erosion', erosion)
	cv.imshow('dilation', dilation)
	cv.waitKey(0)
	cv.destroyAllWindows()
#morph()

# B. morphologyEx // Opening (erosion, dilation) & Closing (dilation, erosion)
def morph_oc():
	img = cv.imread('../Images/14.alphabet.jpg', cv.IMREAD_GRAYSCALE)
	img_o = cv.imread('../Images/15.opening.png', cv.IMREAD_GRAYSCALE)
	img_c = cv.imread('../Images/16.closing.png', cv.IMREAD_GRAYSCALE)
	kernel = np.ones((3, 3), np.uint8)
	opening = cv.morphologyEx(img_o, cv.MORPH_OPEN, kernel)		# Opening 수행
	closing = cv.morphologyEx(img_c, cv.MORPH_CLOSE, kernel)	# Closing 수행
	grad = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)		# Dilation이미지와 Erosion이미지의 차이
	tophat = cv.morphologyEx(img_o, cv.MORPH_TOPHAT, kernel)	# 원본 이미지와 Opening한 이미지의 차이
	blackhat = cv.morphologyEx(img_c, cv.MORPH_BLACKHAT, kernel)# 원본 이미지와 Closing한 이미지의 차이
	cv.imshow('opening', opening)
	cv.imshow('closing', closing)
	cv.imshow('gradient', grad)
	cv.imshow('tophat', tophat)
	cv.imshow('blackhat', blackhat)
	cv.waitKey(0)
	cv.destroyAllWindows()
#morph_oc()

# C. getStructuringElement 커널 매트릭스 만들기
def makekernel():
	M1 = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
	M2 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
	M3 = cv.getStructuringElement(cv.MORPH_CROSS, (5,5))
	print(M1)
	print(M2)
	print(M3)
makekernel()