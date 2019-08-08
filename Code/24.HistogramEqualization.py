# =================================================
# minso.jeong@daum.net
# 24. 이미지 히스토그램 균일화
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# A. Numpy를 이용한 이미지 히스토그램 균일화
def he_numpy():
	img = cv.imread('../Images/30.unequalized.jpg', cv.IMREAD_GRAYSCALE)
	hist, bins = np.histogram(img.ravel(), 256, [0, 256])
	cdf = hist.cumsum()
	cdf_m = np.ma.masked_equal(cdf, 0)										# 0인 부분을 mask 처리
	cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())				# 히스토그램 평활화
	cdf = np.ma.filled(cdf_m, 0).astype('uint8')							# mask 처리 복원
	img2 = cdf[img]
	cv.imshow('Histogram Equalization', img2)
	cv.waitKey(0)
	cv.destroyAllWindows()
#he_numpy()


# B. OpenCV를 이용한 이미지 히스토그램 균일화 
def he_cv():
	img = cv.imread('../Images/30.unequalized.jpg', cv.IMREAD_GRAYSCALE)
	equ = cv.equalizeHist(img)
	res = np.hstack((img, equ))
	cv.imshow('Histogram Equalization', res)
	cv.waitKey(0)
	cv.destroyAllWindows()
he_cv()