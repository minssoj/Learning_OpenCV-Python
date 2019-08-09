# =================================================
# minso.jeong@daum.net
# 26. 2D 이미지 히스토그램 
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

hscale = 10

def hist2D_cv():
	img = cv.imread('../Images/32.flower.jpg')
	hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	# channel [0, 1]: Hue, saturation, Bin 개수 : Hue 180, Saturation 256
	hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
	cv.imshow('hist2D', hist)
	cv.waitKey(0)
	cv.destroyAllWindows()
# hist2D_cv()

def hist2D_plt():
	img = cv.imread('../Images/32.flower.jpg')
	hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	# channel [0, 1]: Hue, saturation, Bin 개수 : Hue 180, Saturation 256
	hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
	plt.imshow(hist, interpolation='nearest')
	plt.show()
#hist2D_plt()

def HSVmap():
	hsvmap = np.zeros((180, 256, 3), np.uint8)
	h, s = np.indices(hsvmap.shape[:2])
	hsvmap[:,:,0] = h
	hsvmap[:,:,1] = s
	hsvmap[:,:,2] = 255
	hsvmap = cv.cvtColor(hsvmap, cv.COLOR_HSV2BGR)
	#cv.imshow('HSVmap', hsvmap)
	#cv.waitKey(0)
	#cv.destroyAllWindows()
	return hsvmap
#HSVmap()

def onChange(x):
	global hscale
	hscale = x

def hist2D():
	img = cv.imread('../Images/32.flower.jpg')
	hsvmap = HSVmap()
	cv.namedWindow('hist2D', 0)
	cv.createTrackbar('scale', 'hist2D', hscale, 32, onChange)

	while True:
		hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
		# hist*0.005*hscale : 히스토그램에서 제외되는 픽셀 조절
		hist = np.clip(hist*0.005*hscale, 0, 1)
		# hist[:, :, np.newaxis] : (180, 256) -> (180, 256, 1)
		hist = hsvmap*hist[:, :, np.newaxis]/255.0
		cv.imshow('hist2D', hist)
		k = cv.waitKey(1) & 0xFF
		if k == 27:
			break
	cv.destroyAllWindows
hist2D()