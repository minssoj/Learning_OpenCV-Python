# =================================================
# minso.jeong@daum.net
# 10. 이미지 Thresholding
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
setting = 3
#img_path = '../Images/07.gradation.jpg'
#img_path = '../Images/08.Koo.jpg'
#img_path = '../Images/09.sudoku.jpg'
img_path = '../Images/10.bimodal.png'

# A. Global Thresholding
def thresholding():
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
def adaptive_thresholding():
	img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
	ret, thr1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
	thr2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
	thr3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
	titles = ['original', 'Global Thresholding(v=127', 'Adaptive MEAN', 'Adaptive GAUSSIAN']
	images = [img, thr1, thr2, thr3]
	for i in range(4):
		cv.imshow(titles[i], images[i])
	cv.waitKey(0)
	cv.destroyAllWindows()

# C. Otsu's Binarization
def otsu():
	img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
	ret, thr1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)					# Globat
	ret, thr2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)	# Otsu
	blur = cv.GaussianBlur(img, (5,5),0)										# Blur + Otsu
	ret, thr3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)	
	titles = ['original_noisy', 'Histogram', 'G-Thresholding', 
			  'original_noisy', 'Histogram', 'Otsu_Thresholding',
			  'Gaussian-filtered', 'Histogram', 'Otsu_Thresholding']
	images = [img, 0, thr1, img, 0, thr2, blur, 0, thr3]
	for i in range(3):
		plt.subplot(3,3,i*3+1), plt.imshow(images[i*3], 'gray')
		plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
		plt.subplot(3,3,i*3+2), plt.hist(images[i*3].ravel(), 256)
		plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
		plt.subplot(3,3,i*3+3), plt.imshow(images[i*3+2], 'gray')
		plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
	plt.show()

if setting == 1:
	thresholding()
elif setting == 2:
	adaptive_thresholding()
elif setting == 3:
	otsu()
