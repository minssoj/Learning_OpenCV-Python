# =================================================
# minso.jeong@daum.net
# 28. 푸리에 변환
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# A. Numpy를 활용한 푸리에 변환
def fourier_np():
	img = cv.imread('../Images/13.yoon.jpg', cv.IMREAD_GRAYSCALE)

	f = np.fft.fft2(img)
	fshift = np.fft.fftshift(f)
	m_spectrum = 20*np.log(np.abs(fshift))

	plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
	plt.title('Input Image'), plt.xticks([]), plt.yticks([])

	plt.subplot(1, 2, 2), plt.imshow(m_spectrum, cmap='gray')
	plt.title('Magnitude Specturm'), plt.xticks([]), plt.yticks([])
	plt.show()
#fourier_np()

# B. OpenCV를 활용한 푸리에 변환
def fourier_cv():
	img = cv.imread('../Images/13.yoon.jpg', cv.IMREAD_GRAYSCALE)

	dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
	dft_shift = np.fft.fftshift(dft)
	m_spectrum = 20*np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

	plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
	plt.title('Input Image'), plt.xticks([]), plt.yticks([])

	plt.subplot(1, 2, 2), plt.imshow(m_spectrum, cmap='gray')
	plt.title('Magnitude Specturm'), plt.xticks([]), plt.yticks([])
	plt.show()

	plt.show()
fourier_cv()


