# =================================================
# minso.jeong@daum.net
# 10. 이미지 Thresholding
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
setting = 1
#img_path = '../Images/07.gradation.jpg'
img_path = '../Images/08.Koo.jpg'

# A. Global Thresholding
if setting == 1:
	img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
	ret, thr1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)		# 임계값보다 작으면 0
	ret, thr2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)	# 임계값보다 크면 0
	ret, thr3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)		# 임계값보다 크면 임계값, 작으면 0
	ret, thr4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)		# 임계값보다 크면 픽셀값, 작으면 0
	ret, thr5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)	# 임계값보다 크면 0, 작으면 픽셀값
	cv.imshow('original', img)
	cv.imshow('binary', thr1)
	cv.imshow('binary_inv', thr2)
	cv.imshow('trunc', thr3)
	cv.imshow('tozero', thr4)
	cv.imshow('tozero_inv', thr5)
	cv.waitKey(0)
	cv.destroyAllWindows()

# B. Adaptive Thresholding
elif setting == 2:
	pass

# C. Otsu's Binarization
elif setting == 3:
	pass
