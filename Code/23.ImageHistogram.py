# =================================================
# minso.jeong@daum.net
# 23. 이미지 히스토그램 이해하기
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def histogram():
	img1 = cv.imread('../Images/29.landscape.jpg', cv.IMREAD_GRAYSCALE)
	img2 = cv.imread('../Images/29.landscape.jpg')
	# 01. OpenCV 함수를 이용해 히스토그램 구하기
	# cv2.calcHist(image, channel, mask, histSize, range)
	hist1 = cv.calcHist([img1], [0], None, [256], [0, 256])
	# 02. numpy를 이용해 히스토그램 구하기
	# numpy.ravel()은 numpy 배열을 1차원으로 바꿔주는 함수
	hist2, bins = np.histogram(img1.ravel(), 256, [0, 256])
	# 03. 1-D 히스토그램의 경우 numpy가 빠름
	hist3 = np.bincount(img1.ravel(), minlength=256)
	# 04. matplotlib으로 히스토그램 그리기
	plt.hist(img1.ravel(), 256, [0, 256])
	# 컬러 이미지 히스토그램 그리기 
	color = ('b', 'g', 'r')
	for i, col in enumerate(color):
		hist = cv.calcHist([img2], [i], None, [256], [0, 256])
		plt.plot(hist, color=col)
		plt.xlim([0, 256])
	plt.show()
histogram()