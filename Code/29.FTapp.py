# =================================================
# minso.jeong@daum.net
# 29. 푸리에 변환 응용
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# A. 푸리에 변환으로 이미지 작업하기
def fourier_edge():
	img = cv.imread('../Images/34.Ji.jpg', cv.IMREAD_GRAYSCALE)

	f = np.fft.fft2(img)
	fshift = np.fft.fftshift(f)

	rows, cols = img.shape
	crow, ccol = int(rows/2), int(cols/2)

	fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
	f_ishift = np.fft.ifftshift(fshift)
	img_back = np.fft.ifft2(f_ishift)
	img_back = np.abs(img_back)

	plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
	plt.title('Original Image'), plt.xticks([]), plt.yticks([])

	plt.subplot(1, 3, 2), plt.imshow(img_back, cmap='gray')
	plt.title('After HPF'), plt.xticks([]), plt.yticks([])

	plt.subplot(1, 3, 3), plt.imshow(img_back)
	plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

	plt.show()

#fourier_edge()

# B. 푸리에 변환을 이용한 이미지 필터 효과
# Averagint Filter
# Gaussian Filter
# Scharr Filter
# sobel_x, sobel_y Filter
# Laplacian Filter
def check_kernel():
	# Simple Averagint Filter without Scaling Parameter
	mean_filter = np.ones((3,3))
	# Creating a Gaussian FIlter
	x = cv.getGaussianKernel(3,3)
	gaussian = x*x.T
	# Filters for Edge Detection
	# Laplacian
	laplacian = np.array([[0, 1, 0],
						  [1,-4, 1],
						  [0, 1, 0]])
	# Scharr in x-direction
	scharr = np.array([[-3, 0, 3],
					   [-10,0,10],
					   [-3, 0, 3]])
	# Sobel in x-direction
	sobel_x = np.array([[-1, 0, 1],
					    [-2, 0, 2],
					    [-1, 0, 1]])
	# Sobel in y-direction
	sobel_y = np.array([[-1,-2,-1],
					    [0, 0, 0],
					    [1, 2, 1]])

	filters = [mean_filter, gaussian, laplacian, sobel_x, sobel_y, scharr]
	filter_name = ['mean_filter', 'gaussian', 'laplacian', 'sobel_x', 'sobel_y', 'scharr_x']

	fft_filters = [np.fft.fft2(x) for x in filters]
	fft_shift = [np.fft.fftshift(y) for y in fft_filters]
	mag_spectrum = [np.log(np.abs(z)+1) for z in fft_shift]

	for i in range(6):
		plt.subplot(2, 3, i+1), plt.imshow(mag_spectrum[i], cmap='gray')
		plt.title(filter_name[i]), plt.xticks([]), plt.yticks([])
	plt.show()

check_kernel()