# =================================================
# minso.jeong@daum.net
# 15. Canny Edge Detection
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def canny():
	img = cv.imread('../Images/13.yoon.jpg', cv.IMREAD_GRAYSCALE)
	edge1 = cv.Canny(img, 50, 200)
	edge2 = cv.Canny(img, 100, 200)
	edge3 = cv.Canny(img, 170, 200)
	plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
	plt.title('original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2), plt.imshow(edge1, cmap='gray')
	plt.title('canny edge1'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3), plt.imshow(edge2, cmap='gray')
	plt.title('canny edge2'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,4), plt.imshow(edge3, cmap='gray')
	plt.title('canny edge3'), plt.xticks([]), plt.yticks([])
	plt.show()
canny()
