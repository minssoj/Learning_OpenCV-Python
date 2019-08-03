# =================================================
# minso.jeong@daum.net
# 12. 이미지 필터링 - blur
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img_path = '../Images/13.yoon.jpg'

# A. 2D Convolution (Image Filtering)
def bluring1():
	img = cv.imread(img_path)
	kernel = np.ones((5, 5), np.float32)/25
	blur = cv.filter2D(img, -1, kernel)
	cv.imshow('original', img)
	cv.imshow('blur', blur)
	cv.waitKey(0)
	cv.destroyAllWindows()

#bluring1()

# B. Image Bluring
def onMouse(x):
	pass

def blurring():
	img = cv.imread(img_path)

	cv.namedWindow('BlurPane')
	cv.createTrackbar('BLUR_MODE', 'BlurPane', 0, 3, onMouse)
	cv.createTrackbar('BLUR', 'BlurPane', 0, 5, onMouse)

	mode = cv.getTrackbarPos('BLUR_MODE', 'BlurPane')
	val = cv.getTrackbarPos('BLUR', 'BlurPane')

	while True:
		val = val*2 + 1
		try:
			if mode == 0:	# Averaging
				blur = cv.blur(img, (val, val))
			elif mode == 1:	# Gaussian Filtering
				blur = cv.GaussianBlur(img, (val, val), 0)
			elif mode == 2:	# Median Filtering - salt & pepper noise 제거 
				blur = cv.medianBlur(img, val)
			elif mode == 3:	# Bilateral Filtering - edge 보존 질감 제거
				blur = cv.bilateralFilter(img, 9, 75, 75)
			else:
				break
			cv.imshow('BlurPane', blur)
		except:
			break

		k = cv.waitKey(1) & 0xFF
		if k == 27:
			break
		mode = cv.getTrackbarPos('BLUR_MODE', 'BlurPane')
		val = cv.getTrackbarPos('BLUR', 'BlurPane')
	cv.destroyAllWindows()

blurring()


