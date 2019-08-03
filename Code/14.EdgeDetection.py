# =================================================
# minso.jeong@daum.net
# 14. 이미지 Gradient를 이용한 경계 찾기
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Laplacian 미분
def grad():
	img = cv.imread('../Images/09.sudoku.jpg', cv.IMREAD_GRAYSCALE)
	laplacian = cv.Laplacian(img, cv.CV_64F)
	sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
	sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
	plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
	plt.title('original'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,2), plt.imshow(laplacian, cmap='gray')
	plt.title('laplacian'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,3), plt.imshow(sobelx, cmap='gray')
	plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
	plt.subplot(2,2,4), plt.imshow(sobely, cmap='gray')
	plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
	plt.show()

#grad()

def grad_type():
	img = cv.imread('../Images/17.box.png', cv.IMREAD_GRAYSCALE)
	sobelx8u = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=5)
	tmp = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
	sobel64f = np.absolute(tmp)
	sobelx8u2 = np.uint8(sobel64f)
	plt.subplot(1,3,1), plt.imshow(img, cmap='gray')
	plt.title('original'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,3,2), plt.imshow(sobelx8u, cmap='gray')
	plt.title('Sobel 8U'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,3,3), plt.imshow(sobelx8u2, cmap='gray')
	plt.title('Sobel 64F'), plt.xticks([]), plt.yticks([])
	plt.show()

grad_type()